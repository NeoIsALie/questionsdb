from sqlalchemy.orm import Session


def get_questions(db: Session, filters):
    query = db.query(
        Question.id,
        Question.question,
        Question.answer
    )

    if filters.company_name is not None:
        query = query.filter(Question.company_name == filters.company_name)

    if filters.job_name is not None:
        query = query.filter(Question.job_mame == filters.job_name)

    return query.all()


def get_question(db: Session, filters):
    query = db.query(
        Question.id,
        Question.question,
        Question.answer
    ).filter(Question.id == filters.question_id)

    return query.one_or_none()


def post_question(**kwargs):
    res = Question.__table__.insert().values(**kwargs)
    return res


def get_companies(db: Session, filters):
    query = db.query(
        Company.id,
        Company.name,
        Company.definition,
        Company.attitude
    )

    if filters.attitude is not None:
        query = query.filter(Company.attitude >= filters.attitude)

    return query.all()


def get_company(db: Session, filters):
    query = db.query(
        Company.id,
        Company.name,
        Company.definition,
        Company.attitude
    ).filter(Company.id == filters.company_id)

    return query.one_or_none()


def post_company(**kwargs):
    res = Company.__table__.insert().values(**kwargs)
    return res


def get_jobs(db: Session, filters):
    query = db.query(
        Job.id,
        Job.name,
        Job.definition,
    )

    if filters.name is not None:
        query = query.filter(Job.name == filters.job_name)

    return query.all()


def get_job(db: Session, filters):
    query = db.query(
        Job.id,
        Job.name,
        Job.definition
    ).filter(Job.id == filters.job_id)

    return query.one_or_none()


def post_job(**kwargs):
    res = Job.__table__.insert().values(**kwargs)
    return res
