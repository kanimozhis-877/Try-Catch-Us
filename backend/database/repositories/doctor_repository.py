from database.repositories.base_repository import BaseRepository
class DoctorRepository(BaseRepository):
    def __init__(self): super().__init__("doctors")
