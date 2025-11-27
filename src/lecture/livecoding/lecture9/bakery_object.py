class BakeryObject:
    def __init__(self, object_id: int, name: str):
        self._id = object_id  # _id should be accessible from derived classes !?
        self._name = name

    """
    id, name properties are read-only (once we create the object, we cannot change its id
    """

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return str(self.id) + " - " + self.name
