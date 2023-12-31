"""Changes migrated!

Revision ID: 86121042216e
Revises: 
Create Date: 2023-09-18 22:37:41.046095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86121042216e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('user_img', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
