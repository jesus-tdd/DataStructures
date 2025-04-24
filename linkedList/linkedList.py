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
