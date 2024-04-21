"""create professor

Revision ID: 20240421183620
Revises: 20240421183459
Create Date: 2024-04-21 20:36:20.572819

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20240421183620"
down_revision = "20240421183459"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "professor",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("specialty", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_professor_birth_date"), "professor", ["birth_date"], unique=False)
    op.create_index(op.f("ix_professor_created_at"), "professor", ["created_at"], unique=False)
    op.create_index(op.f("ix_professor_name"), "professor", ["name"], unique=False)
    op.create_index(op.f("ix_professor_specialty"), "professor", ["specialty"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_index(op.f("ix_professor_specialty"), table_name="professor")
    op.drop_index(op.f("ix_professor_name"), table_name="professor")
    op.drop_index(op.f("ix_professor_created_at"), table_name="professor")
    op.drop_index(op.f("ix_professor_birth_date"), table_name="professor")
    op.drop_table("professor")
    # ### end Alembic commands ###
