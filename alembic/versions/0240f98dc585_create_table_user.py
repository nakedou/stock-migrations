"""create table user

Revision ID: 0240f98dc585
Revises: None
Create Date: 2017-01-08 09:42:48.713723

"""

# revision identifiers, used by Alembic.
revision = '0240f98dc585'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Unicode(64), nullable=False),
        sa.Column('email', sa.Unicode(64), nullable=False),
        sa.Column('password_hash', sa.Unicode(128), nullable=False)
    )


def downgrade():
    op.drop_table('user')
