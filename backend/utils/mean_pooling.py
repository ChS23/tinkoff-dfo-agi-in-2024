import torch


def mean_pooling(model_output: tuple, attention_mask: torch.Tensor) -> torch.Tensor:
    token_embeddings = model_output[0]

    input_mask_expanded = (
        attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    )

    # Умножаем каждый токен на его маску и суммируем
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)

    # Суммируем маски токенов и обрезаем значения, чтобы избежать деления на ноль
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    # Вычисляем усредненный эмбеддинг
    return sum_embeddings / sum_mask