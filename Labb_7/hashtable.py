class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None):
        """key är nyckeln som anvands vid hashningen
        data är det objekt som ska hashas in"""
        self.key = key
        self.data = data

class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.table = [None] * size

    def store(self, key, data):
        """key är nyckeln 
        data är objektet som ska lagras 
        Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.hashfunction(key)
        if self.table[index] is None:
            self.table[index] = [HashNode(key, data)]

        for nod in self.table[index]:
            if nod.key == key:
                nod.data = data
                return

        self.table[index].append(HashNode(key, data))

    def search(self, key):
        """key är nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError """
        index = self.hashfunction(key)
        plats = self.table[index]

        if plats is not None:
            for nod in plats:
                if nod.key == key:
                    return nod.data
        raise KeyError

    def __getitem__(self, key):
        return self.search(key)

    def hashfunction(self, key):
        """key är nyckeln
        Beräknar hashfunktionen för key"""
        result = 0
        for c in key:
            result = result*32 + ord(c)
        return result % self.size
