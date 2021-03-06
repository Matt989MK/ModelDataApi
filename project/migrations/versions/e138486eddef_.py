"""empty message

Revision ID: e138486eddef
Revises: 
Create Date: 2020-10-08 18:45:39.427820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e138486eddef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('bookBase', sa.Integer(), nullable=True),
    sa.Column('bookRecommended', sa.Integer(), nullable=True),
    sa.Column('support', sa.Float(), nullable=True),
    sa.Column('confidence', sa.Float(), nullable=True),
    sa.Column('lift', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recommendations')
    # ### end Alembic commands ###
