from pydantic import BaseModel, Field


class Request(BaseModel):
    query: str = Field(alias="query")


Request.update_forward_refs()
