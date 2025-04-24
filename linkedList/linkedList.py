from ast import Index

from linkedListItem import LinkedListItem as Item

class LinkedList:
    def __init__(self, *items):
        self.__first = None
        self.__last = None
        self.__size = 0
        if len(items) > 0:
            for item in items:
                self.append(item)


    def get(self, index):
        if self.isEmpty():
            raise IndexError("List is empty.")

        if index >= len(self):
            raise IndexError("Index out of bounds.")

        current = self.__first
        for i in range(index):
            current = current.next
        return current.value


    def items(self, reverse = False):
        if self.isEmpty():
            return

        if not reverse:
            current = self.__first
            yield current.value
            while current.hasNext():
                yield current.next.value
                current = current.next
        else:
            current = self.__last
            yield current.value
            while current.hasPrev():
                yield current.prev.value
                current = current.prev


    def append(self, item):
        new_item = Item(item)
        if self.isEmpty():
            self.__first = new_item
        else:
            new_item.prev = self.__last
            self.__last.next = new_item
        self.__last = new_item
        self.__size += 1
        return True

    def pop(self, index=None):
        if self.isEmpty():
            raise IndexError("List is empty.")

        if index is None:
            index = len(self)-1

        if index >= len(self):
            raise IndexError("Index out of bound.")

        if index == 0:
            current = self.__first
            self.__first = self.__first.next
            self.__first.prev = None
            self.__size -= 1
            return current.value

        if index == len(self)-1:
            current = self.__last
            self.__last = self.__last.prev
            self.__last.next = None
            self.__size -= 1
            return current.value

        current = self.__first
        for i in range(0, index):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        self.__size -= 1
        return current.value


    # TODO =========================
    def insert(self, index, item):
        pass


    def remove(self, item):
        pass


    def extend(self, iterable):
        pass


    def index(self, item, start=0, end=None):
        pass


    def count(self, item):
        pass


    def sort(self, key=None, reverse=False):
        pass


    def reverse(self):
        pass
    # TODO =========================


    def clear(self):
        self.__first = None
        self.__last = None
        self.__size = 0


    def copy (self):
        new_list = LinkedList()
        for item in self.items():
            new_list.append(item)
        return new_list


    def isEmpty(self):
        return len(self) == 0


    def __len__(self):
        return self.__size


    def __str__(self):
        if self.isEmpty():
            return "[]"

        string = "["
        for item in self.items():
            string += str(item)+ ", "
        string = string[:-2] + "]"
        return string

if __name__ == "__main__":
    linked_list = LinkedList(1, 2, 3, 2, 7, 1)
    print(linked_list)
    linked_list.append(23)
    print(linked_list)
    linked_list.pop()
    print(linked_list)
    print([item for item in linked_list.items(True)])
    print(len(linked_list))
