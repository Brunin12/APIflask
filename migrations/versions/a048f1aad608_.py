"""empty message

Revision ID: a048f1aad608
Revises: 8fe48b579a38
Create Date: 2023-08-19 09:48:57.468497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a048f1aad608'
down_revision = '8fe48b579a38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('formacao', sa.Column('idade', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('formacao', 'idade')
    # ### end Alembic commands ###