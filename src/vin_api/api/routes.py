from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from ..database.database import get_db
from .models import VinSimpleResponse, VinDecodeResponse, VinDecodeDetail

router = APIRouter(prefix="/api/v1/vin", tags=["vin"])

@router.get("/{vin}/simple", response_model=VinSimpleResponse)
async def validate_vin_simple(vin: str, db: AsyncSession = Depends(get_db)):
    """
    Simple, fast endpoint to validate a VIN by calling scalar functions.
    """
    query = text("""
        SELECT 
            vpic.fvinwmi(:vin) as wmi,
            vpic.fvinmodelyear2(:vin) as model_year,
            vpic.fvincheckdigit(:vin) as check_digit
    """)
    result = await db.execute(query, {"vin": vin})
    row = result.fetchone()
    
    if not row:
        raise HTTPException(status_code=404, detail="VIN information could not be evaluated.")
        
    return VinSimpleResponse(
        vin=vin,
        wmi=row.wmi,
        model_year=row.model_year,
        check_digit=row.check_digit,
        is_valid=row.check_digit is not None and len(str(row.check_digit)) > 0
    )

@router.get("/{vin}/decode", response_model=VinDecodeResponse)
async def validate_vin_complex(vin: str, db: AsyncSession = Depends(get_db)):
    """
    Complex, slower endpoint that returns full decoding information.
    """
    query = text("""
        SELECT variable, value, code, datatype, groupname 
        FROM vpic.spvindecode(:vin)
        WHERE value IS NOT NULL AND value != ''
    """)
    result = await db.execute(query, {"vin": vin})
    rows = result.fetchall()
    
    details = []
    for row in rows:
        details.append(VinDecodeDetail(
            variable=row.variable,
            value=row.value,
            code=row.code,
            group=row.groupname
        ))
        
    return VinDecodeResponse(
        vin=vin,
        details=details
    )
