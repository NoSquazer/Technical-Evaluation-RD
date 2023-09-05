# Python
from sqlalchemy.orm import Session


# SrcUtilities
from sqlalchemy.orm import Session
from src.database.session import SessionLocal


def get_db() -> Session:
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
