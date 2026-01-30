import os
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from qdrant_client import QdrantClient

# Load environment variables
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

QDRANT_URL = os.getenv("url")
QDRANT_API_KEY = os.getenv("Api")

COLLECTION_NAME = "credit_decision_memory"
TOP_K = 10

# Load vector preprocessor
BASE_DIR = Path(__file__).resolve().parent
preprocessor = joblib.load(BASE_DIR / "vector_preprocessor.joblib")

# Init Qdrant client
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=60.0
)

def find_similar_loans(loan_dict, k=TOP_K):
    df = pd.DataFrame([loan_dict])
    X = preprocessor.transform(df)

    if hasattr(X, "toarray"):
        vector = X.toarray()[0].tolist()
    else:
        vector = X[0].tolist()

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=k
    )

    payloads = [r.payload for r in results]
    scores = [r.score for r in results]

    if not payloads:
        return {
            "total_cases": 0,
            "repaid_pct": 0,
            "defaulted_pct": 0,
            "in_progress_pct": 0,
            "fraud_cases": 0,
            "avg_similarity": 0,
            "cases": []
        }

    outcomes = [p.get("loan_outcome") for p in payloads]
    frauds = [p.get("fraud_flag", 0) for p in payloads]

    total = len(outcomes)

    return {
        "total_cases": total,
        "repaid_pct": outcomes.count("Repaid") / total * 100,
        "defaulted_pct": outcomes.count("Defaulted") / total * 100,
        "in_progress_pct": outcomes.count("In Progress") / total * 100,
        "fraud_cases": sum(frauds),
        "avg_similarity": float(np.mean(scores)),
        "cases": payloads
    }
