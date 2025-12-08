class IDEntity(object):
    """
    Class will have:
        1. constructor that takes an id parameter of type int
        2. a property called id that is
            - read-only
            - an int
            - returns the id assigned via the constructor
    """

    def __init__(self, object_id: int):
        self._id = object_id

    @property
    def id(self) -> int:
        return self._id
