import timeit

class Låt:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn


def linsok(lista, mal):
    for x in lista:
        if x == mal:
            return mal
    return None


def binsok(lista, mal):
    vanster = 0
    hoger = len(lista) - 1

    while vanster <= hoger:
        mitten = (vanster + hoger) // 2

        if lista[mitten] == mal:
            return mal
        elif lista[mitten] < mal:
            vanster = mitten + 1
        else:
            hoger = mitten - 1

    return None


def hashsok(hashtabell, mal):
    return hashtabell.get(mal)


def readfile(filnamn):
    lista = []
    with open(filnamn, encoding="utf-8") as fil:
        for rad in fil:
            rad = rad.strip()
            delar = rad.split("<SEP>")
            lista.append(Låt(delar[0], delar[1], delar[2], delar[3]))
        return lista


def main():

    filename = "unique_tracks.txt"
    N = 500000

    lista = readfile(filename)[:N]
    n = len(lista)
    print("Antal element =", n)

    testartist = lista[n//2]


    linjtid = timeit.timeit(
        stmt = lambda: linsok(lista, testartist),
        number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")


    lista.sort()
    bintid = timeit.timeit(
        stmt = lambda: binsok(lista, testartist),
        number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")


    hashtabell = {}
    for låt in lista:
        hashtabell[låt.artistnamn] = låt

    hashtid = timeit.timeit(
        stmt = lambda: hashsok(hashtabell, testartist.artistnamn),
        number = 10000)
    print("Hashtabell sökningen tog", round(hashtid, 4) , "sekunder")


main()