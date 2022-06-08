
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel,Field

class Configuration(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    name: str
    trigger: str
    trigger_args: dict
    service_name: str