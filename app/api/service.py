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
    query = db.query().filter(Question.id == filters.question_id)
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


def get_jobs(db: Session):
    query = db.query(
        Job.id,
        Job.name,
        Job.definition,
    )

    return query.all()


def get_job(job_id, db: Session):
    query = db.query().filter(Job.id == job_id)
    return query.one_or_none()


def post_job(**kwargs):
    res = Job.__table__.insert().values(**kwargs)
    return res


def get_literature(db: Session):
    query = db.query(
        Literature.id,
        Literature.author,
        Literature.title
    )
    return query.all()


def get_book(
        literature_id: int,
        db: Session
):
    query = db.query().filter(Literature.id == literature_id)
    return query.one_or_none()


def add_book(**kwargs):
    res = Literature.__table__.insert().values(**kwargs)
    return res


def get_keywords(db):
    query = db.query(
        Keywords.id,
        Kwywords.keyword
    )
    return query.all()


def post_keyword(**kwargs):
    res = Keywords.__table__.insert().values(**kwargs)
    return res


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
