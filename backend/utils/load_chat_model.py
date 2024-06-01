from transformers import pipeline


def load_chatbot(model: str, device: str = "cuda", torch_dtype: str = "auto"):
    chatbot = pipeline(
        model=model,
        trust_remote_code=True,
        torch_dtype=torch_dtype,
        device_map=device,
        task="conversational",
    )
    return chatbot
