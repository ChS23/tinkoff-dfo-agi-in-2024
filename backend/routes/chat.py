from fastapi import APIRouter, Body, Request
import clickhouse_connect
from transformers import Conversation

from backend import utils
from backend.models import Response, HTTPValidationError, Request as _request
from backend.settings.settings import get_settings

router = APIRouter()

settings = get_settings()
client = clickhouse_connect.get_client(
    host=settings.clickhouse_host,
    port=settings.clickhouse_port
)

SYSTEM_PROMPT = """
INSTRUCT:
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don’t know the answer to a question, please don’t share false information.

If you receive a question that is harmful, unethical, or inappropriate, end the dialogue immediately and do not provide a response. 

If you make a mistake, apologize and correct your answer.

Generate a response based solely on the provided document.

Answer the following question language based only on the CONTEXT provided.

Отвечай только на русском языке.
"""


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
        request: Request,
        input_request: _request = Body(None, title="Request")
) -> Response:
    conversation = Conversation()
    conversation.add_message({"role": "system", "content": SYSTEM_PROMPT})

    ch_response = utils.search_in_clickhouse(
        client,
        settings.clickhouse_table,
        utils.txt2embeddings(
            input_request.query,
            request.app.state.tokenizer,
            request.app.state.model
        )[0]
    )

    conversation = utils.append_documents_to_conversation(conversation, ch_response, limit=3)
    conversation.add_message({"role": "user", "content": input_request.query})

    conversation = utils.generate_answer(
        request.app.state.chatbot,
        conversation,
        temperature=0.2,
        max_new_tokens=2048
    )

    return Response(
        text=conversation[-1]["content"],
        links=list(set([document["url"] for document in ch_response]))
    )
