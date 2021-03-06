"""empty message

Revision ID: 8ee99ed675d4
Revises: 8095f7eda324
Create Date: 2020-10-29 11:57:30.308692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee99ed675d4'
down_revision = '8095f7eda324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_code', sa.String(length=10), nullable=True),
    sa.Column('Course_name', sa.String(length=40), nullable=True),
    sa.Column('Course_Description', sa.String(length=250), nullable=True),
    sa.Column('resources_link', sa.String(length=250), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('Instructor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Instructor_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('course_code')
    )
    op.create_table('Enrolled',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Enrolled')
    op.drop_table('courses')
    # ### end Alembic commands ###
