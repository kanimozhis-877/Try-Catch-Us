from database.repositories.base_repository import BaseRepository


class LabResultRepository(BaseRepository):

    def __init__(self):
        super().__init__("lab_results")