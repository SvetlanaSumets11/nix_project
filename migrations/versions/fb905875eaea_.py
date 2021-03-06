"""empty message

Revision ID: fb905875eaea
Revises: 
Create Date: 2021-07-14 17:40:16.620260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb905875eaea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('director',
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.Column('dir_first_name', sa.String(length=50), nullable=False),
    sa.Column('dir_last_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('director_id')
    )
    op.create_table('genre',
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('genre_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('genre_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_login', sa.String(length=50), nullable=False),
    sa.Column('user_password', sa.String(length=100), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_login')
    )
    op.create_table('film',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('film_name', sa.String(length=50), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('poster', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('film_id')
    )
    op.create_table('film_director',
    sa.Column('film_director_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['director_id'], ['director.director_id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.film_id'], ),
    sa.PrimaryKeyConstraint('film_director_id')
    )
    op.create_table('film_genre',
    sa.Column('film_genre_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['film_id'], ['film.film_id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.genre_id'], ),
    sa.PrimaryKeyConstraint('film_genre_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('film_genre')
    op.drop_table('film_director')
    op.drop_table('film')
    op.drop_table('user')
    op.drop_table('genre')
    op.drop_table('director')
    # ### end Alembic commands ###
