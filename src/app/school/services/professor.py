from src.app.school import repository
from src.app.core import exceptions


class ProfessorService:

    def __init__(self, repository: repository.ProfessorRepository):
        self.repository = repository

    def get_all_stmt(self, name: str = None):
        return self.repository.get_all_stmt(name=name)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_by_id_or_raise(self, id: int):
        record = self.get_by_id(id)
        if not record:
            raise exceptions.CustomError(status_code=404, detail="Professor does not exist")
        return record
