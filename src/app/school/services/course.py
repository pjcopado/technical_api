from src.app.school import repository, schemas as sch, repository


class CourseService:

    def __init__(
        self,
        repository: repository.CourseRepository,
        student_repository: repository.StudentRepository = None,
        professor_repository: repository.ProfessorRepository = None,
    ):
        self.repository = repository
        self.student_repository = student_repository
        self.professor_repository = professor_repository

    def get_all_stmt(self, name: str = None, professor_id: int = None):
        return self.repository.get_all_stmt(name=name, professor_id=professor_id)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_by_id_or_raise(self, id: int):
        return self.repository.get_by_id_or_raise(id)

    def get_students(self, course_id: int):
        return self.repository.get_students(course_id)

    def create(self, obj_in: sch.CourseCreateSch):
        return self.repository.create(obj_in=obj_in)

    def enroll_student(self, course_id: int, student_id: int):
        self.student_repository.get_by_id_or_raise(id=student_id)
        return self.repository.enroll_student(course_id=course_id, student_id=student_id)
