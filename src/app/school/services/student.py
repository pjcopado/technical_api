from src.app.school import repository, schemas as sch, enums
from src.app.core import exceptions


class StudentService:

    def __init__(self, repository: repository.StudentRepository):
        self.repository = repository

    def get_all_stmt(self, name: str = None, career: enums.CareerEnum = None):
        return self.repository.get_all_stmt(name=name, career=career)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_by_id_or_raise(self, id: int):
        record = self.get_by_id(id)
        if not record:
            raise exceptions.CustomError(status_code=404, detail="Student does not exist")
        return record

    def create(self, obj_in: sch.StudentCreateSch):
        return self.repository.create(obj_in=obj_in)

    def get_courses(self, student_id: int):
        return self.repository.get_courses(student_id=student_id)
