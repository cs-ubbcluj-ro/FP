class BakeryEntity:
    """An item identified by its ID in a bakery repository."""

    def __init__(self, object_id: int, name: str):
        self._id = object_id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
