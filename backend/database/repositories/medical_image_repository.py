from database.repositories.base_repository import BaseRepository
class MedicalImageRepository(BaseRepository):
    def __init__(self): super().__init__("medical_images")
