from datetime import date
from sqlalchemy.orm import Session
from .models import College, Program, ProgramCutoff, Scholarship


def seed(db: Session):
    if db.query(College).count() > 0:
        return

    c1 = College(name="Govt Science College", type="govt", state="KA", district="Bengaluru", has_hostel=True, medium="English")
    c2 = College(name="Govt Arts College", type="govt", state="TN", district="Chennai", has_hostel=False, medium="Tamil")
    db.add_all([c1, c2])
    db.flush()

    p1 = Program(college_id=c1.id, name="B.Sc. Chemistry", degree="BSc", duration_months=36)
    p2 = Program(college_id=c1.id, name="B.Sc. Computer Science", degree="BSc", duration_months=36)
    p3 = Program(college_id=c2.id, name="B.A. Economics", degree="BA", duration_months=36)
    db.add_all([p1, p2, p3])
    db.flush()

    db.add_all([
        ProgramCutoff(program_id=p1.id, year=2024, category="GEN", exam="STATE", cutoff_score=85.0),
        ProgramCutoff(program_id=p2.id, year=2024, category="GEN", exam="STATE", cutoff_score=90.0),
        ProgramCutoff(program_id=p3.id, year=2024, category="GEN", exam="STATE", cutoff_score=78.0),
    ])

    db.add_all([
        Scholarship(name="State Merit Scholarship", state="KA", level="UG", amount=20000, deadline=date(2025, 12, 31), provider="State", eligibility_text="Score > 75% in 12th"),
        Scholarship(name="TN First Graduate Scholarship", state="TN", level="UG", amount=15000, deadline=date(2025, 11, 30), provider="State", eligibility_text="First graduate in family"),
        Scholarship(name="National Means Scholarship", state="ALL", level="UG", amount=25000, deadline=None, provider="NSP", eligibility_text="Low income families"),
    ])

    db.commit()


