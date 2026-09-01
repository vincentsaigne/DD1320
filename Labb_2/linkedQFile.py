
class Node:

    def __init__(self, data, next_ = None):
        self.data = data
        self.next = next_


class LinkedQ:

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        ny = Node(data)
        if self.first is None:
            self.first = ny
        else:
            self.last.next = ny
        self.last = ny

    def dequeue(self):
        if self.isEmpty():
            return None

        else:
            data = self.first
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return data.data

    def isEmpty(self):
        if self.first is None:
            return True
        else:
            return False

    def __str__(self):
        kö = []
        nuvarande = self.first
        while nuvarande is not None:
            kö.append(nuvarande.data)
            nuvarande = nuvarande.next
        return f"{kö}"
