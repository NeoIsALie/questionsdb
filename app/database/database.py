import os

from sqlalchemy import create_engine, func
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine(os.environ['DATABASE_URI'])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_postgres_status(db):
    try:
        db.query(func.version()).scalar()
    except OperationalError:
        return False
    return True

