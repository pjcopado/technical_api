from src.app.school import schemas as sch, repository
from src.app.core import exceptions


class CourseService:

    def __init__(self, repository: repository.CourseRepository):
        self.repository = repository

    def get_all_stmt(self, name: list[str] = None, professor_id: int = None):
        return self.repository.get_all_stmt(name=name, professor_id=professor_id)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_by_id_or_raise(self, id: int):
        record = self.get_by_id(id)
        if not record:
            raise exceptions.CustomError(status_code=404, detail="Course does not exist")
        return record

    def get_students(self, course_id: int):
        return self.repository.get_students(course_id=course_id)

    def create(self, obj_in: sch.CourseCreateSch):
        return self.repository.create(obj_in=obj_in)
