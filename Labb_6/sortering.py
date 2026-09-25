import timeit

class Låt:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn

def readfile(filnamn):
    lista = []
    with open(filnamn, encoding="utf-8") as fil:
        for rad in fil:
            rad = rad.strip()
            delar = rad.split("<SEP>")
            lista.append(Låt(delar[0], delar[1], delar[2], delar[3]))
        return lista


def urvalssortera(data):
    n = len(data)
    for i in range(n):
        minst = i
        for j in range(i+1,n):
            if data[j] < data[minst]:
                minst = j
        data[minst],data[i] = data[i], data[minst]

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]

    mindre = []
    storre = []

    for tal in lista[1:]:
        if tal < pivot:
            mindre.append(tal)
        else:
            storre.append(tal)

    return quicksort(mindre) + [pivot] + quicksort(storre)

def main():

    filename = "unique_tracks.txt"
    N = 10000

    lista = readfile(filename)[:N]
    n = len(lista)
    print("Antal element =", n)

    urvalsorttid = timeit.timeit(
        stmt = lambda: urvalssortera(lista),
        number = 1)
    print("Urvalssorteringen tog", round(urvalsorttid, 4) , "sekunder")


    lista2 = readfile(filename)[:N]
    quicksorttid = timeit.timeit(
        stmt = lambda: quicksort(lista2),
        number = 1)
    print("Quicksort sortertingen tog", round(quicksorttid, 4) , "sekunder")

main()
