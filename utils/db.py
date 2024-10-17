from typing import List

import numpy as np
from docarray.index import InMemoryExactNNIndex
from utils.models import VecDBEntry


def search_db(
    db: InMemoryExactNNIndex, condition: str, embeddings_model
) -> List[VecDBEntry]:
    embedding = embeddings_model.embed_query(condition)
    embedding = np.array(embedding)
    matches, scores = db.find(embedding, search_field="embedding", limit=3)
    return matches, scores
