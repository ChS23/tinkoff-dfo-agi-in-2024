def search_in_clickhouse(connection, table_name: str, vector: list[str], limit: int = 5):
    res = []

    vector = ",".join([str(float(i)) for i in vector])

    with connection.query(
            f"""SELECT Id, Source, BusinessLineId, Direction, Product, Type, Description, Title, Url, ParentTitle, ParentUrl, ChunkType, cosineDistance(({vector}), Embedding) as score FROM {table_name} ORDER BY score ASC LIMIT {limit + 500}"""
    ).rows_stream as stream:
        for item in stream:
            _id, source, business_line_id, direction, product, type, description, title, url, parent_title, parent_url, chunk_type, score = item

            # Добавляем результат в список
            res.append(
                {
                    "id": _id,
                    "source": source,
                    "business_line_id": business_line_id,
                    "direction": direction,
                    "product": product,
                    "type": type,
                    "description": description,
                    "title": title,
                    "url": url,
                    "parent_title": parent_title,
                    "parent_url": parent_url,
                    "chunk_type": chunk_type,
                    "distance": score,
                }
            )

    # Возвращаем первые limit результатов
    res = [item for item in res if len(item["description"]) > 100]
    return res[:limit]