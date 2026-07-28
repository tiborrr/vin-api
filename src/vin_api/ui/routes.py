from fastapi import APIRouter, Depends, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from pathlib import Path

from ..database.database import get_db
from ..api.models import VinDecodeDetail

# Setup templates
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

router = APIRouter(tags=["ui"])

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the main search interface.
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@router.get("/ui/validate", response_class=HTMLResponse)
async def validate_vin_ui(
    request: Request,
    vin: str = Query(..., min_length=11, max_length=17),
    db: AsyncSession = Depends(get_db)
):
    """
    HTMX endpoint to validate and decode a VIN, returning an HTML partial.
    """
    # Simple validation first to check check-digit validity quickly
    check_query = text("SELECT vpic.fvincheckdigit(:vin) as check_digit")
    check_result = await db.execute(check_query, {"vin": vin})
    check_row = check_result.fetchone()
    
    if not check_row or check_row.check_digit is None or len(str(check_row.check_digit)) == 0:
        return templates.TemplateResponse(
            request=request,
            name="partials/_vin_error.html",
            context={"error_message": f"The VIN '{vin}' failed checksum validation or does not exist."}
        )
    
    # Perform full decode if check digit is valid
    query = text("""
        SELECT variable, value, code, datatype, groupname 
        FROM vpic.spvindecode(:vin)
        WHERE value IS NOT NULL AND value != ''
    """)
    result = await db.execute(query, {"vin": vin})
    rows = result.fetchall()
    
    if not rows:
        return templates.TemplateResponse(
            request=request,
            name="partials/_vin_error.html",
            context={"error_message": f"No detailed information found for VIN '{vin}'."}
        )
    
    details = []
    for row in rows:
        details.append(VinDecodeDetail(
            variable=row.variable,
            value=row.value,
            code=row.code,
            group=row.groupname
        ))
    
    # Sort details by group for nicer display
    details.sort(key=lambda x: (x.group or "", x.variable))
    
    return templates.TemplateResponse(
        request=request,
        name="partials/_vin_result.html",
        context={
            "result": {
                "vin": vin.upper(),
                "details": details
            }
        }
    )
