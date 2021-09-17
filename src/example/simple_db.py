from typing import Dict, Generic, Optional, TypeVar

T = TypeVar("T")


class Database(Generic[T]):
    def __init__(self) -> None:
        self.db: Dict[int, T] = {}
        self.max_index = 0

    def find(self, index: int) -> Optional[T]:
        return self.db.get(index, None)

    def create(self, data: T) -> int:
        self.db[self.max_index] = data
        user_id = self.max_index
        self.max_index += 1
        return user_id

    def delete(self, index: int) -> Optional[T]:
        return self.db.pop(index, None)
