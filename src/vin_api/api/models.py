from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Any
from datetime import datetime

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
    displayorder: Optional[int] = None

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
    groupname: Optional[str] = None
    variable: Optional[str] = None
    value: Optional[str] = None
    keys: Optional[str] = None
    wmiid: Optional[int] = None
    patternid: Optional[int] = None
    vinschemaid: Optional[int] = None
    elementid: Optional[int] = None
    attributeid: Optional[str] = None
    createdon: Optional[datetime] = None
    code: Optional[str] = None
    datatype: Optional[str] = None
    decode: Optional[str] = None
    source: Optional[str] = None

class Defaultvalue(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    elementid: int
    vehicletypeid: int
    defaultvalue: Optional[str] = None
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

class DefsBody(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    def_: Optional[str] = Field(None, alias="def")
    body_type: Optional[str] = None
    from_year: int
    to_year: Optional[int] = None
    mode: int

class DefsMake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    def_: Optional[str] = Field(None, alias="def")
    ncic_code: Optional[str] = None
    make_type: Optional[str] = None
    from_year: int
    to_year: Optional[int] = None
    mode: int

class DefsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    make: int
    id: int
    def_: Optional[str] = Field(None, alias="def")
    model_type: Optional[str] = None
    includes: Optional[str] = None
    from_year: int
    to_year: Optional[int] = None
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
    code: Optional[str] = None
    lookuptable: Optional[str] = None
    description: Optional[str] = None
    isprivate: Optional[bool] = None
    groupname: Optional[str] = None
    datatype: Optional[str] = None
    minallowedvalue: Optional[int] = None
    maxallowedvalue: Optional[int] = None
    isqs: Optional[bool] = None
    decode: Optional[str] = None
    weight: Optional[int] = None

class Engineconfiguration(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Enginemodel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: Optional[str] = None

class Enginemodelpattern(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    enginemodelid: int
    elementid: int
    attributeid: str
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

class Entertainmentsystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class Errorcode(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    additionalerrortext: Optional[str] = None
    weight: Optional[int] = None

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
    sortorder: Optional[int] = None
    minrangeweight: Optional[int] = None
    maxrangeweight: Optional[int] = None

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
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

class MakeModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    makeid: int
    modelid: int
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

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
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

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
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None
    keys_regex: Optional[str] = None

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
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

class Vehiclespecschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    makeid: int
    createdon: datetime
    updatedon: Optional[datetime] = None
    vehicletypeid: Optional[int] = None
    sourcedate: Optional[datetime] = None
    tobeqced: Optional[bool] = None

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
    displayorder: Optional[int] = None
    formtype: Optional[int] = None
    description: Optional[str] = None
    includeinequipplant: Optional[bool] = None

class Vindescriptor(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    descriptor: str
    modelyear: int
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

class Vinexception(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    vin: str
    checkdigit: bool
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None

class Vinschema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    sourcewmi: Optional[str] = None
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None
    tobeqced: Optional[bool] = None

class Vncsabodytype(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    name: Optional[str] = None

class Vncsamake(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    name: Optional[str] = None

class Vncsamodel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    name: Optional[str] = None
    makeid: Optional[int] = None
    originalid: Optional[int] = None

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
    manufacturerid: Optional[int] = None
    makeid: Optional[int] = None
    vehicletypeid: Optional[int] = None
    createdon: Optional[datetime] = None
    updatedon: Optional[datetime] = None
    countryid: Optional[int] = None
    publicavailabilitydate: Optional[datetime] = None
    trucktypeid: Optional[int] = None
    processedon: Optional[datetime] = None
    noncompliant: Optional[bool] = None
    noncompliantsetbyovsc: Optional[bool] = None

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
    yearto: Optional[int] = None
    orgid: Optional[int] = None

class Wmiyearvalidchars(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    wmi: str
    year: int
    position: Optional[int] = None
    char: Optional[str] = None

class WmiyearvalidcharsCacheexceptions(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    WMI: Optional[Any] = None
    CreatedOn: Optional[Any] = None
    Id: Optional[int] = None

# --- API Response Models ---

class VinSimpleResponse(BaseModel):
    vin: str
    wmi: Optional[str] = None
    model_year: Optional[int] = None
    check_digit: Optional[str] = None
    is_valid: bool

class VinDecodeDetail(BaseModel):
    variable: str
    value: str
    code: str
    group: Optional[str] = None

class VinDecodeResponse(BaseModel):
    vin: str
    details: list[VinDecodeDetail]
