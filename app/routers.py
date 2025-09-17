from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from .db import get_db
from . import models, schemas

router = APIRouter()


@router.get("/colleges", response_model=list[schemas.College])
def list_colleges(
    state: str | None = Query(None),
    district: str | None = Query(None),
    type: str | None = Query(None),
    has_hostel: bool | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(models.College)
    if state:
        q = q.filter(models.College.state == state)
    if district:
        q = q.filter(models.College.district == district)
    if type:
        q = q.filter(models.College.type == type)
    if has_hostel is not None:
        q = q.filter(models.College.has_hostel == has_hostel)
    return q.all()


@router.get("/programs", response_model=list[schemas.Program])
def list_programs(collegeId: int | None = None, degree: str | None = None, db: Session = Depends(get_db)):
    q = db.query(models.Program)
    if collegeId:
        q = q.filter(models.Program.college_id == collegeId)
    if degree:
        q = q.filter(models.Program.degree == degree)
    return q.all()


@router.get("/programs/{program_id}/cutoffs", response_model=list[schemas.ProgramCutoff])
def program_cutoffs(program_id: int, year: int | None = None, db: Session = Depends(get_db)):
    q = db.query(models.ProgramCutoff).filter(models.ProgramCutoff.program_id == program_id)
    if year:
        q = q.filter(models.ProgramCutoff.year == year)
    return q.all()


@router.get("/scholarships", response_model=list[schemas.Scholarship])
def list_scholarships(state: str | None = None, db: Session = Depends(get_db)):
    q = db.query(models.Scholarship)
    if state:
        q = q.filter((models.Scholarship.state == state) | (models.Scholarship.state == "ALL"))
    return q.all()


@router.post("/scholarships/match", response_model=schemas.ScholarshipMatchResponse)
def match_scholarships(req: schemas.ScholarshipMatchRequest, db: Session = Depends(get_db)):
    # Simple rule-based matching demo
    items = db.query(models.Scholarship).all()
    matches = []
    for s in items:
        score = 0.0
        why: list[str] = []
        if s.state in (req.student_state, "ALL"):
            score += 0.6
            why.append("state match")
        if s.level == req.level:
            score += 0.3
            why.append("level match")
        if s.amount >= 20000:
            score += 0.1
            why.append("good amount")
        if score > 0:
            matches.append({"scholarship_id": s.id, "score": round(score, 2), "why": why})
    matches.sort(key=lambda m: m["score"], reverse=True)
    return {"matches": matches}


@router.post("/career-paths/simulate")
def simulate_career_paths():
    # Minimal stubbed response
    return {
        "pathNodes": [
            {"label": "B.Sc. Chemistry", "node_type": "course"},
            {"label": "M.Sc. Chemistry", "node_type": "degree"},
            {"label": "Analyst", "node_type": "job", "median_salary": 450000},
        ],
        "transitions": [[0, 1], [1, 2]],
        "scenarios": [{"outcomes": "Entry analyst role in pharma", "probabilities": 0.65}],
    }


@router.get("/tests")
def list_tests():
    return [
        {"id": 1, "title": "Aptitude Test", "type": "aptitude"},
        {"id": 2, "title": "Interest Survey", "type": "interest"},
    ]


