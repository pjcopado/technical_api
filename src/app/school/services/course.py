from src.app.school import schemas as sch, repository
from src.app.school.services import StudentService
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

    def enroll_student(self, student_service: StudentService, course_id: int, student_id: int):
        course_obj_db = self.get_by_id_or_raise(id=course_id)
        student_obj_db = student_service.get_by_id_or_raise(id=student_id)
        return self.repository.enroll_student(course_id=course_id, student_id=student_id)
