from array import array

class ArrayQ:
    def __init__(self):
        self.__kö = array("i", [])

    def enqueue(self, data):
        self.__kö.append(data)

    def dequeue(self):
        return self.__kö.pop(0)

    def isEmpty(self):
        if len(self.__kö) == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(list(self.__kö))

