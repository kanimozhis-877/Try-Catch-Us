from database.repositories.base_repository import BaseRepository
class PatientRepository(BaseRepository):
    def __init__(self): super().__init__("patients")
