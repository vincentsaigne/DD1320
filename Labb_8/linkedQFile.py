class Node:

    def __init__(self, data, next_ = None):
        self.data = data
        self.next = next_


class LinkedQ:

    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, data):
        ny = Node(data)
        if self.__first is None:
            self.__first = ny
        else:
            self.__last.next = ny
        self.__last = ny

    def dequeue(self):
        if self.isEmpty():
            return None

        else:
            data = self.__first
            self.__first = self.__first.next
            if self.__first is None:
                self.__last = None
            return data.data

    def isEmpty(self):
        if self.__first is None:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return None
        return self.__first.data

    def __str__(self):
        sträng = ""
        nuvarande = self.__first
        while nuvarande is not None:
            sträng += str(nuvarande.data)
            nuvarande = nuvarande.next
        return sträng
