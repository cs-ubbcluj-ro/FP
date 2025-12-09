from lecture.livecoding.bakery.domain.bakery_object import BakeryObject
from lecture.livecoding.bakery.repo.memory_repo import MemoryRepository


class AbstractTextFileRepo(MemoryRepository):
    def __init__(self, file_name: str):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def store(self, element: BakeryObject):
        super().store(element)
        # self._save_file()

    def remove(self, element: BakeryObject):
        super().remove(element)
        # self._save_file()

    def find(self, element_id: int) -> BakeryObject:
        return super().find(element_id)

    def _load_file(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def _save_file(self):
        raise NotImplementedError("Must be implemented in subclasses")
