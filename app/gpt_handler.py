import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def get_gpt_feedback(resume: str, jd: str) -> str:
    prompt = f"""
    Analyze the following resume and job description.
    Identify skill gaps and suggest 3 improvements:

    Resume:
    {resume}

    Job Description:
    {jd}
    """

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  # fallback to a valid model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
