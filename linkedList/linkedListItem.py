class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


    def hasNext(self):
        return self.next is not None

    def hasPrev(self):
        return self.prev is not None


    def __str__(self):
        return str(self.value)