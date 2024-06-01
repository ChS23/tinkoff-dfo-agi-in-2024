from transformers import AutoModel, AutoTokenizer


def load_models(model: str, device: str = "cpu", torch_dtype: str = "auto") -> tuple:

    # Загружаем токенизатор
    tokenizer = AutoTokenizer.from_pretrained(
        model, device_map=device, torch_dtype=torch_dtype
    )

    # Загружаем модель
    model = AutoModel.from_pretrained(model, device_map=device, torch_dtype=torch_dtype)

    return tokenizer, model