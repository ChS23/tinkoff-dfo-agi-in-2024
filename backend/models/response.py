from typing import List

from pydantic import BaseModel, Field


class Response(BaseModel):
    text: str = Field(alias="text")
    links: List[str] = Field(alias="links")


Response.update_forward_refs()
