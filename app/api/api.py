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


@router.post("/questions/{question_id}")
def question(
        question_id: int,
        body: QuestionBodySchema,
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


@router.post("/companies/{company_id}")
def question(
        company_id: int,
        body: CompanyBodySchema,
):
    filters = IdFilterSchema(
        question_id=company_id
    )
    return service.get_company(db, filters)


@router.post("/companies/")
def add_question(**kwargs):
    return service.post_company(**kwargs)

