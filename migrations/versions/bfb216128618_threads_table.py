"""Threads Table

Revision ID: bfb216128618
Revises: f93598bd52e5
Create Date: 2020-09-26 23:01:05.513352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfb216128618'
down_revision = 'f93598bd52e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('thread',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=50), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_thread_created'), 'thread', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_thread_created'), table_name='thread')
    op.drop_table('thread')
    # ### end Alembic commands ###