"""init database

Revision ID: 6bf6b2c8af42
Revises: 
Create Date: 2022-11-25 23:48:11.050567

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6bf6b2c8af42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'literature',
        sa.Column('id', sa.Integer(), autoincrement=True),
        sa.Column('title', sa.String()),
        sa.Column('author', sa.String()),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'questions',
        sa.Column('id', sa.BigInteger(), autoincrement=True),
        sa.Column('question', sa.Text()),
        sa.Column('answer', sa.Text(), nullable=True),
        sa.Column('literature_id', sa.BigInteger),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(["literature_id"], ["literature.id"], name="fk_literature_id")
    )

    op.create_table(
        'companies',
        sa.Column('id', sa.Integer(), autoincrement=True),
        sa.Column('title', sa.String(256), nullable=False),
        sa.Column('definition', sa.Text(), nullable=True),
        sa.Column('attitude', sa.types.Numeric(1, 1), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer(), autoincrement=True),
        sa.Column('title', sa.String(256), nullable=False),
        sa.Column('definition', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'keywords',
        sa.Column('id', sa.Integer(), autoincrement=True),
        sa.Column('keyword', sa.Text),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'unification',
        sa.Column('id', sa.BigInteger(), autoincrement=True),
        sa.Column('job', sa.BigInteger()),
        sa.Column('compamy', sa.BigInteger()),
        sa.Column('keywords', sa.Integer()),
        sa.Column('questions', sa.BigInteger()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['job'], ['jobs.id'], name='fk_job_id'),
        sa.ForeignKeyConstraint(['company'], ['companies.id'], name='fk_company_id'),
        sa.ForeignKeyConstraint(['keywords'], ['keywords.id'], name='fk_keywords_id'),
        sa.ForeignKeyConstraint(['questions'], ['questions.id'], name='fk_questions_id')
    )


def downgrade() -> None:
    op.drop_table('unification')
    op.drop_table('kwywords')
    op.drop_table('jobs')
    op.drop_table('companies')
    op.drop_table('questions')
    op.drop_table('literature')
