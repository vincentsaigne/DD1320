import csv

class Kdrama:

    def __init__(self, kdrama):
        self.name = kdrama[0]
        self.rating = float(kdrama[1])
        self.actors = kdrama[2]
        self.viewship = float(kdrama[3])
        self.genre = kdrama[4]
        self.director = kdrama[5]
        self.writer = kdrama[6]
        self.year = int(kdrama[7])
        self.n_episodes = int(kdrama[8])
        self.network = kdrama[9]

    def __str__(self):
        return f"{self.name} ({self.year}) - Genre: {self.genre} - Rating {self.rating}"

    def __lt__(self, annan):
        return self.rating < annan.rating

    def hämta_genre(self):
        return self.genre

    def populäritet(self):
        return self.rating * self.viewship

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
        hashkod = self.hashfunction(key)
        index = hashkod % self.size
        if self.table[index] is None:
            self.table[index] = [HashNode(key, data)]
        else:
            self.table[index].append(HashNode(key, data))

    def search(self, key):
        """key är nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError """
        hashkod = self.hashfunction(key)
        index = hashkod % self.size
        plats = self.table[index]

        if plats is not None:
            for nod in plats:
                if nod.key == key:
                    return nod.data
        else:
            raise KeyError

    def __getitem__(self, key):
        return self.search(key)

    def hashfunction(self, key):
        """key är nyckeln
        Beräknar hashfunktionen för key"""
        result = 0
        for c in key:
            result = result*32 + ord(c)
        return result


def läs_csv_fil_till_lista(filnamn):
    kdramadict = Hashtable(1000)
    with open(filnamn, mode="r", encoding="utf-8") as kdramafil:
        csvfil = csv.reader(kdramafil, delimiter=",")
        next(csvfil)
        for rad in csvfil:
            nykdrama = Kdrama(rad)
            kdramadict.store(nykdrama.name, nykdrama)
    return kdramadict


def main():
    kdramadict = läs_csv_fil_till_lista("kdrama.csv") 
    print(kdramadict["Legend of the Blue Sea"])
    print(kdramadict["The Heirs"])
    print(kdramadict["Twinkling Watermelon"])

main()