
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

def putta(p, newvalue):
    # Funktion som gör själva jobbet att stoppa in en ny nod
    if p is None:
        return Node(newvalue)
    elif newvalue < p.value:
        p.left = putta(p.left, newvalue)
    elif newvalue > p.value:
        p.right = putta(p.right, newvalue)
    return p

def finns(p, value):
    # Funktion som gör själva jobbet att söka efter ett värde
    if p is None:
        return False
    if p.value == value:
        return True
    if value < p.value:
        return finns(p.left, value)
    if p.value < value:
        return finns(p.right, value)

def skriv(p):
    # Funktion som gör själva jobbet att skriva ut trädet
    if p is not None:
        skriv(p.left)
        print(p.value, end=" ")
        skriv(p.right)
