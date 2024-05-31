from typing import List, Optional

from pydantic import BaseModel, Field

from ..models.validation_error import ValidationError


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(alias="detail", default=None)


HTTPValidationError.update_forward_refs()
