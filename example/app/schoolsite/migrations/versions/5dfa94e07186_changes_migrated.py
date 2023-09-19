"""Changes migrated!

Revision ID: 5dfa94e07186
Revises: 86121042216e
Create Date: 2023-09-19 06:30:24.237257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dfa94e07186'
down_revision = '86121042216e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exam_question_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('summary', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exam_choice_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('choice_text', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['exam_question_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exam_choice_model')
    op.drop_table('exam_question_model')
    # ### end Alembic commands ###