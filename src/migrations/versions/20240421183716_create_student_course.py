"""create student_course

Revision ID: 20240421183716
Revises: 20240421183646
Create Date: 2024-04-21 20:37:17.022078

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20240421183716"
down_revision = "20240421183646"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "student_course",
        sa.Column("course_id", sa.Integer(), nullable=False),
        sa.Column("student_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["course_id"], ["course.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["student_id"], ["student.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("course_id", "student_id"),
    )
    op.create_index(op.f("ix_student_course_course_id"), "student_course", ["course_id"], unique=False)
    op.create_index(op.f("ix_student_course_created_at"), "student_course", ["created_at"], unique=False)
    op.create_index(op.f("ix_student_course_student_id"), "student_course", ["student_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_index(op.f("ix_student_course_student_id"), table_name="student_course")
    op.drop_index(op.f("ix_student_course_created_at"), table_name="student_course")
    op.drop_index(op.f("ix_student_course_course_id"), table_name="student_course")
    op.drop_table("student_course")
    # ### end Alembic commands ###
