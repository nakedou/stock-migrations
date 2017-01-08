"""create table stock_holders

Revision ID: 46993bacafe4
Revises: 895d5537d6fd
Create Date: 2017-01-08 18:33:30.944915

"""

# revision identifiers, used by Alembic.
revision = '46993bacafe4'
down_revision = '895d5537d6fd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'stock_holders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('stock_code', sa.String(6), nullable=False),
        sa.Column('reg_day', sa.String(10), nullable=False),
        sa.Column('holders', sa.Integer, nullable=False),
        sa.Column('change_percent', sa.Float),
        sa.Column('c_m_j_z', sa.Float),
        sa.Index('idx_stock_code', 'stock_code')
    )


def downgrade():
    op.drop_table('stock_holders')
