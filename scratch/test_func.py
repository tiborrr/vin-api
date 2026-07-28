from sqlalchemy import func, select
from sqlalchemy.dialects import postgresql

vin = "1234"

sp_func = func.vpic.spvindecode(vin).table_valued(
    "variable", "value", "code", "datatype", "groupname"
)
query = select(sp_func).where(sp_func.c.value.isnot(None), sp_func.c.value != '')

print(query.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))

query2 = select(
    func.vpic.fvinwmi(vin).label("wmi"),
    func.vpic.fvinmodelyear2(vin).label("model_year"),
    func.vpic.fvincheckdigit(vin).label("check_digit")
)

print(query2.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
