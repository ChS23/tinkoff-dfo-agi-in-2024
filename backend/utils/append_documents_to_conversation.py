def append_documents_to_conversation(conversation, documents, limit: int = 3):
    if limit > len(documents):
        texts = [document["description"] for document in documents]
    else:
        texts = [document["description"] for document in documents[:limit]]

    text = "\n".join(texts)

    document_template = f"""
    CONTEXT:
    {text}
    Отвечай только на русском языке.

    ВОПРОС:
    """
    conversation.add_message({"role": "user", "content": document_template})

    return conversation