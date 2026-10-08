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

class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, nyckel, data):
        self.dict[nyckel] = data

    def search(self, nyckel):
        try:
            return self.dict[nyckel]
        except KeyError:
            return "Datan finns inte"

    def __getitem__(self, nyckel):
        return self.search(nyckel)

    def __contains__(self, nyckel):
        return nyckel in self.dict

def läs_csv_fil_till_lista(filnamn):
    kdramadict = DictHash()
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
    print(kdramadict["Obefintlig kdrama"])

main()