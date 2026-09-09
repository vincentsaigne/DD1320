svenska = []
with open("word3.txt", encoding="utf-8") as svenskafil:
    for rad in svenskafil:
        ordet = rad.strip()
        svenska.append(ordet)

bokstäver = "abcdefghijklmnopqrstuvwxyzåäö"
def makechildren(nuvarande):
    for i in range(3):
        for b in bokstäver:
            nytt_barn = nuvarande[:i] + b + nuvarande[i+1:]

            if nytt_barn in svenska and nytt_barn not in gamla:
                print(nytt_barn)
                gamla.append(nytt_barn)

startord = input("\nStartord: ")
slutord = input("Slutord: ")
if len(startord) != 3 or len(slutord) != 3:
    print("\nOrden måste vara tre tecken långt")
    exit()

gamla = []
gamla.append(startord)
makechildren(startord)
