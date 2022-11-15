from pydantic import BaseModel


class IdFilterSchema(BaseModel):
    question_id: int = None


class QuestionBodySchema(BaseModel):
    question_id: int = None,
    question: str = None,
    answer: str = None


class QuestionsBodySchema(BaseModel):
    company_name: str = None
    job_name: str = None


class ManyFieldFilterSchema(BaseModel):
    company_name: str = None
    job_name: str = None
