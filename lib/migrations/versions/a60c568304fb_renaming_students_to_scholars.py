"""Renaming students to scholars

Revision ID: a60c568304fb
Revises: 791279dd0760
Create Date: 2025-03-04 17:12:13.653231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a60c568304fb'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')



def downgrade() -> None:
    op.rename_table('scholars','students')
