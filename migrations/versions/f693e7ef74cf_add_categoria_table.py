"""Add categoria table

Revision ID: f693e7ef74cf
Revises: d9eb7f5642f4
Create Date: 2023-03-17 22:03:39.221676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f693e7ef74cf'
down_revision = 'd9eb7f5642f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('imagen', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias')
    # ### end Alembic commands ###
