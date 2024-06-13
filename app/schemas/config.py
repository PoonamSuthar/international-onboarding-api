from pydantic import BaseModel
from typing import Dict, Any

class ConfigBase(BaseModel):
    country_code: str
    requirements: Dict[str, Any]

class ConfigCreate(ConfigBase):
    pass

class ConfigUpdate(ConfigBase):
    pass

class ConfigOut(ConfigBase):
    class Config:
        orm_mode = True
