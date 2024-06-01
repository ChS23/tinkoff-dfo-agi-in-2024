from typing import List, Union
import torch

from backend.utils.mean_pooling import mean_pooling


def txt2embeddings(
    text: Union[str, List[str]], tokenizer, model, device: str = "cpu"
) -> torch.Tensor:
    # Кодируем входной текст с помощью токенизатора
    if isinstance(text, str):
        text = [text]
    encoded_input = tokenizer(
        text,
        padding=True,
        truncation=True,
        return_tensors="pt",
        max_length=512,
    )
    # Перемещаем закодированный ввод на указанное устройство
    encoded_input = {k: v.to(device) for k, v in encoded_input.items()}

    # Получаем выход модели для закодированного ввода
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Преобразуем выход модели в векторное представление текста
    return mean_pooling(model_output, encoded_input["attention_mask"])