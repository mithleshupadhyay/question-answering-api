from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def validate_questions(question_data, context):
    """Validates the relevance of questions using cosine similarity."""
    context_embedding = embedding_model.encode(context)
    for question in question_data["questions"]["mcq"]:
        question_embedding = embedding_model.encode(question["question"])
        score = cosine_similarity([context_embedding], [question_embedding])[0][0]
        question["source"]["confidence_score"] = round(score, 2)

    for question in question_data["questions"]["open_ended"]:
        question_embedding = embedding_model.encode(question["question"])
        score = cosine_similarity([context_embedding], [question_embedding])[0][0]
        question["source"]["confidence_score"] = round(score, 2)
    return question_data
