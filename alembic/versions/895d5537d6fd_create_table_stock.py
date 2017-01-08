"""create table stock

Revision ID: 895d5537d6fd
Revises: 0240f98dc585
Create Date: 2017-01-08 18:33:19.910381

"""

# revision identifiers, used by Alembic.
revision = '895d5537d6fd'
down_revision = '0240f98dc585'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'stock',
        sa.Column('j_y_s', sa.String(2), nullable=False),
        sa.Column('code', sa.String(6), nullable=False),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Index('idx_code', 'code'),
        sa.Index('idx_j_y_s_code', 'j_y_s')
    )


def downgrade():
    op.drop_table('stock')
