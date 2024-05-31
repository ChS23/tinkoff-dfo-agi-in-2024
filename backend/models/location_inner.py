from pydantic import BaseModel


class LocationInner(BaseModel):
    pass


LocationInner.update_forward_refs()
