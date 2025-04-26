from linkedListItem import LinkedListItem as Item

class LinkedList:
    def __init__(self, *items):
        self.__first = None
        self.__last = None
        self.__size = 0
        if len(items) > 0:
            for item in items:
                self.append(item)


    def get(self, element_index):
        if self.isEmpty():
            raise IndexError("List is empty.")

        if element_index >= len(self):
            raise IndexError("Index out of bounds.")

        current = self.__first
        for i in range(element_index):
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


    def __insert_item(self, item:Item) -> None:
        self.__size += 1

        if not item.hasPrev() and not item.hasNext():
            self.__first = item
            self.__last = item
            return

        if not item.hasPrev():
            self.__first = item
            item.next.prev = item
            return

        if not item.hasNext():
            self.__last = item
            item.prev.next = item
            return

        item.prev.next = item
        item.next.prev = item
        return


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
            return self.__insert_item(Item(item))
        return self.__insert_item(Item(item, prev_item=self.__last))


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
            return self.__insert_item(Item(item, next_item=self.__first))

        current = self.__first
        for i in range(index-1):
            current = current.next
        return self.__insert_item(Item(item, current, current.next))


    def remove(self, item):
        current = self.__first
        if current is None:
            raise ValueError("There is not such item.")

        while current.value != item:
            if not current.hasNext():
                raise ValueError("There is not such item.")
            current = current.next

        return self.__remove_item(current)

    def extend(self, iterable) -> None:
        for item in iterable:
            self.append(item)


    def index(self, item, start=0, end=None) -> int:
        i = 0
        if end is None:
            end = len(self)

        for element in self.items():
            if start <= i < end:
                if element == item:
                    return i
            i += 1

        raise ValueError(f"Item '{item}' not found.")


    def count(self, item) -> int :
        counter = 0
        for element in self.items():
            if item == element:
                counter += 1
        return counter


    # TODO
    def sort(self, key=None, reverse=False):
        pass


    def reverse(self) -> None:
        items = [item for item in self.items(True)]
        self.clear()
        for item in items:
            self.append(item)


    def clear(self) -> None:
        self.__first = None
        self.__last = None
        self.__size = 0


    def copy (self):
        new_list = LinkedList()
        for item in self.items():
            new_list.append(item)
        return new_list


    def isEmpty(self) -> bool:
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
    linked_list.append(20)
    print(linked_list)
    linked_list.insert(0,1)
    print(linked_list)
    linked_list.insert(5, 30)
    print(linked_list)
    linked_list.insert(len(linked_list), 40)
    print(linked_list)
