from .pdf_handler import extract_pdf_content
from .llm_handler import generate_questions
from .validation import validate_questions

def process_pdf(pdf_path, topic):
    """Processes the PDF and generates validated questions."""
    content = extract_pdf_content(pdf_path)
    results = []
    for section in content:
        question_data = generate_questions(topic, section["content"])
        validated_data = validate_questions(question_data, section["content"])
        results.append({
            "page_number": section["page_number"],
            "questions": validated_data
        })
    return results
