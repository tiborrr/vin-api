from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Abs(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Adaptivecruisecontrol(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Adaptivedrivingbeam(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Airbaglocations(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Airbaglocfront(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Airbaglocknee(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Autobrake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Automaticpedestrainalertingsound(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Autoreversesystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Axleconfiguration(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Batterytype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Bedtype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Blindspotintervention(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Blindspotmonitoring(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Bodycab(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Bodystyle(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Brakesystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Busfloorconfigtype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Bustype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class CanAacn(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Chargerlevel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Combinedbrakingsystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Conversion(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    fromelementid: int
    toelementid: int
    formula: str

class Coolingtype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Country(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    displayorder: int | None = None

class Custommotorcycletype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Daytimerunninglight(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Decodingoutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    addedon: datetime
    groupname: str | None = None
    variable: str | None = None
    value: str | None = None
    keys: str | None = None
    wmiid: int | None = None
    patternid: int | None = None
    vinschemaid: int | None = None
    elementid: int | None = None
    attributeid: str | None = None
    createdon: datetime | None = None
    code: str | None = None
    datatype: str | None = None
    decode: str | None = None
    source: str | None = None

class Defaultvalue(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    elementid: int
    vehicletypeid: int
    defaultvalue: str | None = None
    createdon: datetime | None = None
    updatedon: datetime | None = None

class DefsBody(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    def_: str | None = Field(None, alias="def")
    body_type: str | None = None
    from_year: int
    to_year: int | None = None
    mode: int

class DefsMake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    def_: str | None = Field(None, alias="def")
    ncic_code: str | None = None
    make_type: str | None = None
    from_year: int
    to_year: int | None = None
    mode: int

class DefsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    make: int
    id: int
    def_: str | None = Field(None, alias="def")
    model_type: str | None = None
    includes: str | None = None
    from_year: int
    to_year: int | None = None
    mode: int

class Destinationmarket(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Drivetype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Dynamicbrakesupport(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Ecs(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Edr(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Electrificationlevel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Element(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    code: str | None = None
    lookuptable: str | None = None
    description: str | None = None
    isprivate: bool | None = None
    groupname: str | None = None
    datatype: str | None = None
    minallowedvalue: int | None = None
    maxallowedvalue: int | None = None
    isqs: bool | None = None
    decode: str | None = None
    weight: int | None = None

class Engineconfiguration(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Enginemodel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None = None

class Enginemodelpattern(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    enginemodelid: int
    elementid: int
    attributeid: str
    createdon: datetime | None = None
    updatedon: datetime | None = None

class Entertainmentsystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Errorcode(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    additionalerrortext: str | None = None
    weight: int | None = None

class Evdriveunit(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Forwardcollisionwarning(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Fueldeliverytype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Fueltankmaterial(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Fueltanktype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Fueltype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Grossvehicleweightrating(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    sortorder: int | None = None
    minrangeweight: int | None = None
    maxrangeweight: int | None = None

class Keylessignition(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Lanecenteringassistance(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Lanedeparturewarning(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Lanekeepsystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Lowerbeamheadlamplightsource(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Make(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    createdon: datetime | None = None
    updatedon: datetime | None = None

class MakeModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    makeid: int
    modelid: int
    createdon: datetime | None = None
    updatedon: datetime | None = None

class Manufacturer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class ManufacturerMake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    manufacturerid: int
    makeid: int

class Model(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    createdon: datetime | None = None
    updatedon: datetime | None = None

class Motorcyclechassistype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Motorcyclesuspensiontype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Nonlanduse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Parkassist(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Pattern(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vinschemaid: int
    keys: str
    elementid: int
    attributeid: str
    createdon: datetime | None = None
    updatedon: datetime | None = None
    keys_regex: str | None = None

class Pedestrianautomaticemergencybraking(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Pretensioner(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Rearautomaticemergencybraking(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Rearcrosstrafficalert(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Rearvisibilitycamera(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Seatbeltsall(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Semiautomaticheadlampbeamswitching(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Steering(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Tpms(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Tractioncontrol(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Trailerbodytype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Trailertype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Transmission(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Turbo(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Valvetraindesign(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Vehiclespecpattern(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vspecschemapatternid: int
    iskey: bool
    elementid: int
    attributeid: str
    createdon: datetime | None = None
    updatedon: datetime | None = None

class Vehiclespecschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    makeid: int
    createdon: datetime
    updatedon: datetime | None = None
    vehicletypeid: int | None = None
    sourcedate: datetime | None = None
    tobeqced: bool | None = None

class VehiclespecschemaModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vehiclespecschemaid: int
    modelid: int

class VehiclespecschemaYear(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vehiclespecschemaid: int
    year: int

class Vehicletype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    displayorder: int | None = None
    formtype: int | None = None
    description: str | None = None
    includeinequipplant: bool | None = None

class Vindescriptor(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    descriptor: str
    modelyear: int
    createdon: datetime | None = None
    updatedon: datetime | None = None

class Vinexception(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vin: str
    checkdigit: bool
    createdon: datetime | None = None
    updatedon: datetime | None = None

class Vinschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    sourcewmi: str | None = None
    createdon: datetime | None = None
    updatedon: datetime | None = None
    tobeqced: bool | None = None

class Vncsabodytype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    name: str | None = None

class Vncsamake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    name: str | None = None

class Vncsamodel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int | None = None
    name: str | None = None
    makeid: int | None = None
    originalid: int | None = None

class Vspecschemapattern(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    schemaid: int

class Wheelbasetype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Wheeliemitigation(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Wmi(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    wmi: str
    manufacturerid: int | None = None
    makeid: int | None = None
    vehicletypeid: int | None = None
    createdon: datetime | None = None
    updatedon: datetime | None = None
    countryid: int | None = None
    publicavailabilitydate: datetime | None = None
    trucktypeid: int | None = None
    processedon: datetime | None = None
    noncompliant: bool | None = None
    noncompliantsetbyovsc: bool | None = None

class WmiMake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    wmiid: int
    makeid: int

class WmiVinschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    wmiid: int
    vinschemaid: int
    yearfrom: int
    yearto: int | None = None
    orgid: int | None = None

class Wmiyearvalidchars(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    wmi: str
    year: int
    position: int | None = None
    char: str | None = None

class WmiyearvalidcharsCacheexceptions(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    WMI: Any | None = None
    CreatedOn: Any | None = None
    Id: int | None = None

# --- API Response Models ---

class VinSimpleResponse(BaseModel):
    vin: str
    wmi: str | None = None
    descriptor: str | None = None
    model_year: int | None = None
    check_digit: str | None = None
    is_valid: bool

class VinDecodeDetail(BaseModel):
    variable: str
    value: str
    code: str
    group: str | None = None

class VinDecodeResponse(BaseModel):
    vin: str
    details: list[VinDecodeDetail]

class VinBulkRequest(BaseModel):
    vins: list[str] = Field(..., max_length=100)

class VinBulkResponse(BaseModel):
    results: list[VinSimpleResponse]
