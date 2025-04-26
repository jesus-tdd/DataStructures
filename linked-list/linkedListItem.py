class LinkedListItem:
    def __init__(self, value, prev_item=None, next_item=None):
        self.value = value
        self.next = next_item
        self.prev = prev_item


    def hasNext(self):
        return self.next is not None

    def hasPrev(self):
        return self.prev is not None


    def __str__(self):
        return str(self.value)
