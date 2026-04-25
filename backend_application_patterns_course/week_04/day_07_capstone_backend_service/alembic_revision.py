"""create catalog items table

Revision ID: 20260425_create_catalog_items
Revises:
Create Date: 2026-04-25
"""

from alembic import op
import sqlalchemy as sa


revision = '20260425_create_catalog_items'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'bap_w4d7_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=120), nullable=False, unique=True),
        sa.Column('status', sa.String(length=30), nullable=False, server_default='draft'),
        sa.Column('is_deleted', sa.Boolean(), nullable=False, server_default=sa.false()),
    )


def downgrade() -> None:
    op.drop_table('bap_w4d7_items')
