"""create course

Revision ID: 20240421183646
Revises: 20240421183620
Create Date: 2024-04-21 20:36:46.464213

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20240421183646"
down_revision = "20240421183620"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "course",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("professor_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("duration_value", sa.Integer(), nullable=False),
        sa.Column("duration_unit", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["professor_id"], ["professor.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_course_created_at"), "course", ["created_at"], unique=False)
    op.create_index(op.f("ix_course_duration_unit"), "course", ["duration_unit"], unique=False)
    op.create_index(op.f("ix_course_duration_value"), "course", ["duration_value"], unique=False)
    op.create_index(op.f("ix_course_name"), "course", ["name"], unique=False)
    op.create_index(op.f("ix_course_professor_id"), "course", ["professor_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_index(op.f("ix_course_professor_id"), table_name="course")
    op.drop_index(op.f("ix_course_name"), table_name="course")
    op.drop_index(op.f("ix_course_duration_value"), table_name="course")
    op.drop_index(op.f("ix_course_duration_unit"), table_name="course")
    op.drop_index(op.f("ix_course_created_at"), table_name="course")
    op.drop_table("course")
    # ### end Alembic commands ###
