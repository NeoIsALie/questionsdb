import sqlalchemy as sa

from app.database.database import Base


class Literature(Base):
    __tablename__ = 'literature'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    author = sa.Column(sa.String)


class Question(Base):
    __tablename__ = "questions"

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    question = sa.Column(sa.Text)
    answer = sa.Column(sa.Text, nullable=True)
    literature_id = sa.Column(sa.BigInteger, sa.ForeignKey('literature.id'))


class Company(Base):
    __tablename__ = "companies"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(256))
    definition = sa.Column(sa.Text, nullable=True)
    attitude = sa.Column(sa.types.Numeric(1, 1), nullable=True)


class Job(Base):
    __tablename__ = "jobs"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(256))
    definition = sa.Column(sa.Text, nullable=True)


class Keyword(Base):
    __tablename__ = "keywords"
    id = sa.Column(sa.Integer, primary_key=True)
    keyword = sa.Column(sa.Text)


class Unification(Base):
    __tablename__ = "unification"

    id = sa.Column(sa.BigInteger, primary_key=True)
    job = sa.Column(sa.Integer, sa.ForeignKey("jobs.id"))
    company = sa.Column(sa.Integer, sa.ForeignKey("companies.id"))
    keywords = sa.Column(sa.Integer, sa.ForeignKey("keywords.id"))
    questions = sa.Column(sa.BigInteger, sa.ForeignKey("questions.id"))
