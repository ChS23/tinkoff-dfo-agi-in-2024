from transformers import Conversation


def generate_answer(
    chatbot,
    conversation: Conversation,
    max_new_tokens: int = 8000,
    temperature=0.7,
    top_k: int = 50,
    top_p: float = 0.95,
    repetition_penalty: float = 2.0,
    do_sample: bool = True,
    num_beams: int = 2,
    early_stopping: bool = True,
) -> str:

    conversation = chatbot(
        conversation,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=do_sample,
        num_beams=num_beams,
        early_stopping=early_stopping,
    )

    # Возвращаем последнее сообщение чатбота как ответ
    return conversation
