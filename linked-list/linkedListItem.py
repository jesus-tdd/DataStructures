class LinkedListItem:
    def __init__(self, value, prev_item=None, next_item=None):
        self.value = value
        self.next = next_item
        self.prev = prev_item


    def hasNext(self) -> bool:
        return self.next is not None

    def hasPrev(self) -> bool:
        return self.prev is not None


    def __lt__(self, other) -> bool:
        if not isinstance(other, LinkedListItem):
            return False
        return self.value < other.value


    def __str__(self) -> str:
        return str(self.value)
