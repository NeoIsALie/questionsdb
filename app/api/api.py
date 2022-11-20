from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import service
from app.api.schemas import ManyFieldFilterSchema, QuestionBodySchema, \
    QuestionsBodySchema, IdFilterSchema

router = APIRouter()


@router.get("/ping")
def ping():
    return 1


@router.post("/questions")
def questions(
        body: QuestionsBodySchema,
        db: Session = Depends(get_db)
):
    filters = ManyFieldFilterSchema(
        company_name=body.company_name,
        job_name=body.job_name,
    )
    return service.get_questions(db, filters)


@router.get("/questions/{question_id}")
def question(
        question_id: int,
        body: QuestionBodySchema,
        db: Session = Depends(get_db)
):
    filters = IdFilterSchema(
        question_id=question_id
    )
    return service.get_question(db, filters)


@router.post("/questions/")
def add_question(**kwargs):
    return service.post_question(**kwargs)


@router.post("/companies")
def companies(
        body: CompanyBodySchema,
        db: Session = Depends(get_db)
):
    filters = ManyFieldFilterSchema(
        attitude=body.attitude,
    )
    return service.get_companies(db, filters)


@router.get("/companies/{company_id}")
def company(
        company_id: int,
        body: CompanyBodySchema,
        db: Session = Depends(get_db)
):
    filters = IdFilterSchema(
        question_id=company_id
    )
    return service.get_company(db, filters)


@router.post("/companies/")
def add_question(**kwargs):
    return service.post_company(**kwargs)


@router.get("/literature")
def literature(
        body: LiteratureSchema,
        db: Depends(get_db)
):
    return service.get_literature(db)


@router.get("/literature/{literature_id}")
def get_book(
        literature_id: int,
        db: Depends(get_db)
):
    return service.get_book(literature_id, db)


@router.post("/literature/")
def add_literature(
        **kwargs
):
    return service.add_book(**kwargs)


@router.get("/jobs")
def get_jobs(
        db: Depends(get_db)
):
    return service.get_jobs(db)


@router.get("/jobs/{job_id}")
def get_job(
        job_id: int,
        db: Depends(get_db)
):
    return service.get_job(job_id, db)


@router.post("/jobs/")
def add_job(**kwargs):
    return service.post_job(**kwargs)


@router.get("/keywords")
def get_keywords(
        db: Depends(get_db)
):
    return service.get_keywords(db)


@router.post("/keywords/")
def add_keyword(
        **kwargs
):
    return service.post_keyword(**kwargs)

