"""empty message

Revision ID: f0e99f411d81
Revises: d705e6f095e4
Create Date: 2021-07-17 17:39:40.307100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0e99f411d81'
down_revision = 'd705e6f095e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'genre', ['genre_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'genre', type_='unique')
    # ### end Alembic commands ###
