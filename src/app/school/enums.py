import enum


class CareerEnum(str, enum.Enum):
    COMPUTER_SCIENCE = "Computer Science"
    ENGINEERING = "Engineering"
    MATHEMATICS = "Mathematics"
    PHYSICS = "Physics"
    BIOLOGY = "Biology"
    CHEMISTRY = "Chemistry"
    SOCIOLOGY = "Sociology"
    ECONOMICS = "Economics"

    @classmethod
    def to_list(cls):
        return list(map(lambda c: c.value, cls))


class CourseDurationUnitEnum(str, enum.Enum):
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
