from src.app.school import repository, schemas as sch, enums


class ProfessorService:

    def __init__(self, repository: repository.ProfessorRepository):
        self.repository = repository

    def get_all_stmt(self, name: str = None, age_ge: int = None, age_le: int = None, specialty: enums.CareerEnum = None):
        return self.repository.get_all_stmt(name=name, age_ge=age_ge, age_le=age_le, specialty=specialty)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_by_id_or_raise(self, id: int):
        return self.repository.get_by_id_or_raise(id)

    def create(self, obj_in: sch.StudentCreateSch):
        return self.repository.create(obj_in=obj_in)

    def get_courses(self, professor_id: int):
        return self.repository.get_courses(professor_id=professor_id)
