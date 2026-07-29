from functools import lru_cache
from pathlib import Path

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..api.models import VinDecodeDetail
from ..constants import SP_VIN_DECODE_COLUMNS
from ..database.database import get_db


# Setup templates
@lru_cache
def get_templates():
    base_dir = Path(__file__).resolve().parent.parent
    return Jinja2Templates(directory=str(base_dir / "templates"))

router = APIRouter(tags=["ui"])

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, templates: Jinja2Templates = Depends(get_templates)):
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
    db: AsyncSession = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates)
):
    """
    HTMX endpoint to validate and decode a VIN, returning an HTML partial.
    """
    # Simple validation first to check check-digit validity quickly
    check_query = select(
        func.vpic.fvincheckdigit(vin).label("check_digit"),
        func.vpic.fvindescriptor(vin).label("descriptor")
    )
    check_result = await db.execute(check_query)
    check_row = check_result.fetchone()
    
    if not check_row or check_row.check_digit is None or len(str(check_row.check_digit)) == 0:
        return templates.TemplateResponse(
            request=request,
            name="partials/_vin_error.html",
            context={"error_message": f"The VIN '{vin}' failed checksum validation or does not exist."}
        )
    
    # Perform full decode if check digit is valid
    sp_func = func.vpic.spvindecode(vin).table_valued(*SP_VIN_DECODE_COLUMNS)
    query = select(sp_func).where(sp_func.c.value.isnot(None), sp_func.c.value != '')
    result = await db.execute(query)
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
                "descriptor": check_row.descriptor if check_row else None,
                "details": details
            }
        }
    )
