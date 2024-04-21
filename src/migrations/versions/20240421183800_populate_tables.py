"""create student_course

Revision ID: 20240421183800
Revises: 20240421183716
Create Date: 2024-04-21 20:38:00.022078

"""

import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20240421183800"
down_revision = "20240421183716"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "student",
            sa.column("id", sa.Integer),
            sa.column("name", sa.String),
            sa.Column("birth_date", sa.Date),
            sa.column("career", sa.String),
        ),
        [
            {
                "id": 1,
                "name": "John",
                "birth_date": datetime.date.fromisoformat("2004-01-01"),
                "career": "Computer Science",
            },
            {
                "id": 2,
                "name": "Alice",
                "birth_date": datetime.date.fromisoformat("2002-01-01"),
                "career": "Engineering",
            },
            {
                "id": 3,
                "name": "Bob",
                "birth_date": datetime.date.fromisoformat("2003-01-01"),
                "career": "Mathematics",
            },
            {
                "id": 4,
                "name": "Emma",
                "birth_date": datetime.date.fromisoformat("2001-01-01"),
                "career": "Physics",
            },
            {
                "id": 5,
                "name": "Michael",
                "birth_date": datetime.date.fromisoformat("2002-01-01"),
                "career": "Biology",
            },
            {
                "id": 6,
                "name": "Sophia",
                "birth_date": datetime.date.fromisoformat("2004-01-01"),
                "career": "Chemistry",
            },
            {
                "id": 7,
                "name": "William",
                "birth_date": datetime.date.fromisoformat("2003-01-01"),
                "career": "Engineering",
            },
            {
                "id": 8,
                "name": "Olivia",
                "birth_date": datetime.date.fromisoformat("2002-01-01"),
                "career": "Sociology",
            },
            {
                "id": 9,
                "name": "James",
                "birth_date": datetime.date.fromisoformat("2003-01-01"),
                "career": "Economics",
            },
            {
                "id": 10,
                "name": "Emily",
                "birth_date": datetime.date.fromisoformat("2004-01-01"),
                "career": "Engineering",
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "professor",
            sa.column("id", sa.Integer),
            sa.column("name", sa.String),
            sa.Column("birth_date", sa.Date),
            sa.column("specialty", sa.String),
        ),
        [
            {
                "id": 1,
                "name": "Dr. Smith",
                "birth_date": datetime.date.fromisoformat("1989-01-01"),
                "specialty": "Computer Science",
            },
            {
                "id": 2,
                "name": "Prof. Johnson",
                "birth_date": datetime.date.fromisoformat("1969-01-01"),
                "specialty": "Engineering",
            },
            {
                "id": 3,
                "name": "Dr. Brown",
                "birth_date": datetime.date.fromisoformat("1984-01-01"),
                "specialty": "Mathematics",
            },
            {
                "id": 4,
                "name": "Prof. Wilson",
                "birth_date": datetime.date.fromisoformat("1976-01-01"),
                "specialty": "Physics",
            },
            {
                "id": 5,
                "name": "Dr. Martinez",
                "birth_date": datetime.date.fromisoformat("1972-01-01"),
                "specialty": "Biology",
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "course",
            sa.column("id", sa.Integer),
            sa.column("name", sa.String),
            sa.Column("duration_value", sa.Integer),
            sa.Column("duration_unit", sa.String),
            sa.column("professor_id", sa.Integer),
        ),
        [
            {
                "id": 1,
                "name": "Introduction to Programming",
                "duration_value": 12,
                "duration_unit": "week",
                "professor_id": 1,
            },
            {
                "id": 2,
                "name": "Mechanics and Dynamics",
                "duration_value": 10,
                "duration_unit": "week",
                "professor_id": 4,
            },
            {
                "id": 3,
                "name": "Calculus I",
                "duration_value": 14,
                "duration_unit": "week",
                "professor_id": 3,
            },
            {
                "id": 4,
                "name": "Cell Biology",
                "duration_value": 8,
                "duration_unit": "week",
                "professor_id": 5,
            },
            {
                "id": 5,
                "name": "Data Structures and Algorithms",
                "duration_value": 16,
                "duration_unit": "week",
                "professor_id": 1,
            },
        ],
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    pass
    # ### end Alembic commands ###
