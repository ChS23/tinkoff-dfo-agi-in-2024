from fastapi import APIRouter, Body

from ..models import Response, HTTPValidationError, Request

router = APIRouter()


@router.post(
    "/assist",
    responses={
        200: {"model": Response, "description": "Successful Response"},
        422: {"model": HTTPValidationError, "description": "Validation Error"},
    },
    tags=["default"],
    summary="Assist",
    response_model_by_alias=True,
)
async def assist_assist_post(
    request: Request = Body(None, title="Request")
) -> Response:
    return Response(
        text="Hello, World!",
        links=["https://www.example.com"],
    )
