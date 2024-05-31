from typing import List

from pydantic import BaseModel, Field

from ..models.location_inner import (LocationInner)


class ValidationError(BaseModel):
    loc: List[LocationInner] = Field(alias="loc")
    msg: str = Field(alias="msg")
    type: str = Field(alias="type")


ValidationError.update_forward_refs()
