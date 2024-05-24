from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

class Score(BaseModel):
    score: int

app = FastAPI()


@app.get("/")
async def respond_scores():
    return "1,1,1,1,1,1,1,1,1,1"


@app.post("/")
def receive_score(score: Score):
    print(score.score)
