from ast import Index
from operator import index

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


    def __remove_item(self, item:Item):
        self.__size -= 1
        if not item.hasPrev() and not item.hasNext():
            self.__first = None
            self.__last = None
            return item.value

        if not item.hasPrev():
            self.__first = item.next
            item.next.prev = None
            return item.value

        if not item.hasNext():
            self.__last = item.prev
            item.prev.next = None
            return item.value

        item.prev.next = item.next
        item.next.prev = item.prev
        return item.value


    def append(self, item) -> None:
        if self.isEmpty():
            self.__first = Item(item)
            self.__last = self.__first
            self.__size += 1
            return
        self.__last = Item(item, prev_item=self.__last)
        self.__last.prev.next = self.__last
        self.__size += 1

    def pop(self, index=None):
        if self.isEmpty():
            raise IndexError("List is empty.")

        if index is None:
            index = len(self)-1

        if index >= len(self):
            raise IndexError("Index out of bounds.")

        current = self.__first
        for i in range(0, index):
            current = current.next
        return self.__remove_item(current)


    def insert(self, index, item) -> None:
        if index > len(self):
            raise IndexError("Index out of bounds.")

        if index == 0:
            self.__first = Item(item, next_item=self.__first)
            if not self.__first.hasNext():
                self.__last = self.__first
            else:
                self.__first.next.prev = self.__first
            self.__size += 1
            return


        current = self.__first
        for i in range(index-1):
            current = current.next

        new_item = Item(item, current, current.next)
        current.next = new_item
        if new_item.hasNext():
            new_item.next.prev = new_item
        self.__size += 1


    def remove(self, item):
        current = self.__first
        if current is None:
            raise ValueError("There is not such item.")

        while current.value != item:
            if not current.hasNext():
                raise ValueError("There is not such item.")
            current = current.next

        return self.__remove_item(current)

    def extend(self, iterable):
        for item in iterable:
            self.append(item)


    def index(self, item, start=0, end=None):
        i = 0
        if end is None:
            end = len(self)

        for element in self.items():
            if start <= i < end:
                if element == item:
                    return i
            i += 1

        raise ValueError(f"Item '{item}' not found.")


    # TODO =========================
    def count(self, item):
        pass


    def sort(self, key=None, reverse=False):
        pass
    # TODO =========================


    def reverse(self):
        items = [item for item in self.items(True)]
        self.clear()
        for item in items:
            self.append(item)


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
    linked_list.insert(len(linked_list), 20)
    linked_list.insert(len(linked_list), 30)
    print(linked_list)
    linked_list.pop(linked_list.index(20))
    print(linked_list)