from database.repositories.base_repository import BaseRepository
class QRSessionRepository(BaseRepository):
    def __init__(self): super().__init__("qr_sessions")
