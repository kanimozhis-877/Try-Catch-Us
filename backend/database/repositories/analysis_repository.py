from database.repositories.base_repository import BaseRepository
class AnalysisRepository(BaseRepository):
    def __init__(self): super().__init__("analyses")
