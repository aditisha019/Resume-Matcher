from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import compute_similarity
from app.gpt_handler import get_gpt_feedback
import uvicorn

app = FastAPI()

class Input(BaseModel):
    resume: str
    job_description: str

@app.post("/analyze")
def analyze(data: Input):
    score = compute_similarity(data.resume, data.job_description)
    feedback = get_gpt_feedback(data.resume, data.job_description)
    return {"match_score": score, "suggestions": feedback}
