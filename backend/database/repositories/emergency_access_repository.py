from database.repositories.base_repository import BaseRepository
class EmergencyAccessRepository(BaseRepository):
    def __init__(self): super().__init__("emergency_access")
