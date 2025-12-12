from lecture.livecoding.bakery.domain.bakery_object import BakeryObject
from lecture.livecoding.bakery.repo.memory_repo import MemoryRepository


class AbstractTextFileRepo(MemoryRepository):
    """
    This is an abstract class (abstract = it cannot/should not be instantiated)
    Its job is to figure out when save_file and load_file must be called
    Derived classes should implement those methods for storing BakeyObject instances
    """

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

    def _load_file(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def _save_file(self):
        raise NotImplementedError("Must be implemented in subclasses")
