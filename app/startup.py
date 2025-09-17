from sqlalchemy.orm import Session
from .db import engine, Base, SessionLocal
from .seed import seed


def init_db():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        seed(db)
    finally:
        db.close()


