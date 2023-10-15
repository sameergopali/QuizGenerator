
from pydantic import BaseModel, Field
from typing import List

class Question(BaseModel):
    question: str = Field(description="Questions")
    choices: List[str] = Field(description="Available options for a multiple-choice question")
    correct: str = Field(description="correct answer index")

class Quiz(BaseModel):
    quiz: List[Question]