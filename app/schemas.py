from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class ProgramCutoff(BaseModel):
    id: int
    year: int
    category: str
    exam: str
    cutoff_score: float | None

    class Config:
        from_attributes = True


class Program(BaseModel):
    id: int
    name: str
    degree: str
    duration_months: int
    cutoffs: List[ProgramCutoff] = []

    class Config:
        from_attributes = True


class College(BaseModel):
    id: int
    name: str
    type: str
    state: str
    district: str
    has_hostel: bool
    medium: str
    programs: List[Program] = []

    class Config:
        from_attributes = True


class Scholarship(BaseModel):
    id: int
    name: str
    state: str
    level: str
    amount: int
    deadline: Optional[date]
    provider: str
    eligibility_text: str

    class Config:
        from_attributes = True


class ScholarshipMatchRequest(BaseModel):
    student_state: str
    level: str = "UG"


class ScholarshipMatchResult(BaseModel):
    scholarship_id: int
    score: float
    why: list[str]


class ScholarshipMatchResponse(BaseModel):
    matches: list[ScholarshipMatchResult]


