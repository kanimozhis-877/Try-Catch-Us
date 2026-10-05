from database.repositories.base_repository import BaseRepository
class ComparisonRepository(BaseRepository):
    def __init__(self): super().__init__("comparisons")
