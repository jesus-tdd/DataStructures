from linkedListItem import LinkedListItem as Item

class LinkedList:
    def __init__(self, *items):
        self.__first = None
        self.__last = None
        self.__size = 0
        if len(items) > 0:
            self.add(*items)


    def items(self):
        if self.isEmpty():
            return

        current = self.__first
        yield current
        while current.hasNext():
            yield current.next
            current = current.next


    def add(self, *items):
        if len(items) > 1:
            for item in items:
                if not self.add(item):
                    return False
            return True

        new_item = Item(*items)
        if self.isEmpty():
            self.__first = new_item
        else:
            new_item.prev = self.__last
            self.__last.next = new_item
        self.__last = new_item
        self.__size += 1
        return True


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
    print(LinkedList(1, 2))
