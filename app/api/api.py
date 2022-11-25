from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import service

router = APIRouter()


@router.get("/ping")
def ping():
    return 1


@router.post("/questions")
def questions(
        db: Session = Depends(get_db),
        company_name: str = None,
        job_name: str = None
):
    return service.get_questions(db, company_name, job_name)


@router.get("/questions/{question_id}")
def question(
        db: Session = Depends(get_db),
        question_id: int
):
    return service.get_question(db, question_id)


@router.post("/questions/")
def add_question(**kwargs):
    return service.post_question(**kwargs)

@router.delete("/questions/{id}")
def delete_question(
        db: Session = Depends(get_db),
        question_id: int
):
    return service.delete_question(db, question_id)


@router.post("/companies")
def companies(
        db: Session = Depends(get_db),
        attitude: int = None
):
    return service.get_companies(db, attitude)


@router.get("/companies/{company_id}")
def company(
        db: Session = Depends(get_db),
        company_id: int
):
    return service.get_company(db, company_id)


@router.post("/companies/")
def add_question(**kwargs):
    return service.post_company(**kwargs)

@router.delete("/companies/{id}")
def delete_company(
        db: Session = Depends(get_db),
        company_id: int
):
    return service.delete_company(db, company_id)


@router.get("/literature")
def literature(
        db: Depends(get_db)
):
    return service.get_literature(db)


@router.get("/literature/{literature_id}")
def get_book(
        db: Depends(get_db),
        literature_id: int,
):
    return service.get_book(db, literature_id)


@router.post("/literature/")
def add_literature(
        **kwargs
):
    return service.add_book(**kwargs)

@router.delete("/literature/{id}")
def delete_question(
        db: Session = Depends(get_db),
        literature_id: int
):
    return service.delete_book(db, literature_id)

@router.get("/jobs")
def get_jobs(
        db: Depends(get_db)
):
    return service.get_jobs(db)


@router.get("/jobs/{job_id}")
def get_job(
        db: Depends(get_db),
        job_id: int
):
    return service.get_job(db, job_id)


@router.post("/jobs/")
def add_job(**kwargs):
    return service.post_job(**kwargs)

@router.delete("/jobs/{id}")
def delete_question(
        db: Session = Depends(get_db),
        job_id: int
):
    return service.delete_job(db, job_id)


@router.get("/keywords")
def get_keywords(
        db: Depends(get_db)
):
    return service.get_keywords(db)


@router.post("/keywords/")
def add_keyword(**kwargs):
    return service.post_keyword(**kwargs)

@router.delete("/keywords/{id}")
def delete_question(
        db: Session = Depends(get_db),
        keyword_id: int
):
    return service.delete_keyword(db, keyword_id)