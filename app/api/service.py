from sqlalchemy.orm import Session

from app.databasee.models import *


def get_questions(db: Session, company_name, job_name):
    query = db.query(
        Question.id,
        Question.question,
        Question.answer
    )

    if company_name:
        query = query.filter(Question.company_name == company_name)

    if job_name:
        query = query.filter(Question.job_mame == job_name)

    return query.all()


def get_question(db: Session, question_id):
    query = db.query().filter(Question.id == question_id)
    return query.one_or_none()


def post_question(**kwargs):
    res = Question.__table__.insert().values(**kwargs)
    return res


def delete_question(db: Session, question_id: int):
    question = get_question(db, question_id)
    if question:
        db.delete(question)


def get_companies(db: Session, attitude: int =None):
    query = db.query(
        Company.id,
        Company.name,
        Company.definition,
        Company.attitude
    )

    if attitude:
        query = query.filter(Company.attitude >= attitude)

    return query.all()


def get_company(db: Session, company_id: int):
    query = db.query(
        Company.id,
        Company.name,
        Company.definition,
        Company.attitude
    ).filter(Company.id == company_id)

    return query.one_or_none()


def post_company(**kwargs):
    res = Company.__table__.insert().values(**kwargs)
    return res


def delete_company(db: Session, company_id: int):
    company = get_question(db, company_id)
    if company:
        db.delete(company)


def get_jobs(db: Session):
    query = db.query(
        Job.id,
        Job.name,
        Job.definition,
    )

    return query.all()


def get_job(db: Session, job_id: int):
    query = db.query().filter(Job.id == job_id)
    return query.one_or_none()


def post_job(**kwargs):
    res = Job.__table__.insert().values(**kwargs)
    return res


def delete_job(db: Session, job_id: int):
    job = get_job(db, job_id)
    if job:
        db.delete(job)


def get_literature(db: Session):
    query = db.query(
        Literature.id,
        Literature.author,
        Literature.title
    )
    return query.all()


def get_book(
        db: Session,
        literature_id: int
):
    query = db.query().filter(Literature.id == literature_id)
    return query.one_or_none()


def add_book(**kwargs):
    res = Literature.__table__.insert().values(**kwargs)
    return res


def delete_book(db: Session, literature_id: int):
    book = get_book(db, literature_id)
    if book:
        db.delete(book)


def get_keywords(db):
    query = db.query(
        Keyword.id,
        Keyword.keyword
    )
    return query.all()


def get_keyword(db: Session, keyword_id: int):
    query = db.query(
        Keyword.id,
        Keyword.keyword
    ).filter(Keyword.id == keyword_id)
    return query.one_or_none()


def post_keyword(**kwargs):
    res = Keyword.__table__.insert().values(**kwargs)
    return res


def delete_keyword(db: Session, keyword_id: int):
    keyword = get_keyword(db, keyword_id)
    if keyword:
        db.delete(keyword)


def get_unification(db: Session):
    query = db.query(
        Unification.id,
        Unification.job,
        Unification.keywords,
        Unification.question
    )
    return query.all()


def post_unification(**kwargs):
    res = Unification.__table__.insert().values(**kwargs)
    return res
