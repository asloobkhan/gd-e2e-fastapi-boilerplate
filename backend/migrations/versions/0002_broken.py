"""e2e broken migration

Revision ID: 0002_broken
Revises: 0001_baseline
"""
from alembic import op

revision = "0002_broken"
down_revision = "0001_baseline"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE table_that_does_not_exist ADD COLUMN e2e_flag integer")


def downgrade() -> None:
    pass