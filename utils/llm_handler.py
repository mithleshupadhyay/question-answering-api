import openai
import json

# Set your OpenAI API key
openai.api_key = ""

def generate_questions(topic, context):
    """Generates questions using GPT-4."""
    prompt = f"""
You are an advanced question generation system. Based on the topic '{topic}' and the following context:
---
{context}
---
Generate 15 multiple-choice questions and 5 open-ended questions. Provide answers, explanations, and include source information.
Output in this JSON format:
{{
    "questions": {{
        "mcq": [
            {{
                "id": "MCQ-1",
                "topic": "{topic}",
                "type": "MCQ",
                "question": "...",
                "options": ["..."],
                "correct_answer": "...",
                "explanation": "...",
                "source": {{
                    "page_number": ...,
                    "confidence_score": ...
                }}
            }}
        ],
        "open_ended": [
            {{
                "id": "OE-1",
                "topic": "{topic}",
                "type": "open_ended",
                "question": "...",
                "model_answer": "...",
                "key_points": ["..."],
                "source": {{
                    "page_number": ...,
                    "context": "...",
                    "confidence_score": ...
                }}
            }}
        ]
    }}
}}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return json.loads(response['choices'][0]['message']['content'])
