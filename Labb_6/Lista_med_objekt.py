class Låt:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn

låtlista = []
with open("unique_tracks.txt", encoding="utf-8") as fil:
    for rad in fil:
        rad = rad.strip()
        delar = rad.split("<SEP>")
        låtlista.append(Låt(delar[0], delar[1], delar[2], delar[3]))

print(len(låtlista))
print(låtlista[0].låttitel)
print(låtlista[-1].låttitel)
