"""create student

Revision ID: 20240421183459
Revises:
Create Date: 2024-04-21 20:34:59.934877

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20240421183459"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "student",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("career", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_student_birth_date"), "student", ["birth_date"], unique=False)
    op.create_index(op.f("ix_student_career"), "student", ["career"], unique=False)
    op.create_index(op.f("ix_student_created_at"), "student", ["created_at"], unique=False)
    op.create_index(op.f("ix_student_name"), "student", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_index(op.f("ix_student_name"), table_name="student")
    op.drop_index(op.f("ix_student_created_at"), table_name="student")
    op.drop_index(op.f("ix_student_career"), table_name="student")
    op.drop_index(op.f("ix_student_birth_date"), table_name="student")
    op.drop_table("student")
    # ### end Alembic commands ###
