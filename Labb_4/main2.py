from linkedQFile import LinkedQ

svenska = []
with open("word3.txt", encoding="utf-8") as svenskafil:
    for rad in svenskafil:
        ordet = rad.strip()
        svenska.append(ordet)

BOKSTÄVER = "abcdefghijklmnopqrstuvwxyzåäö"
def makechildren(nuvarande_ord):
    for i in range(3):
        for b in BOKSTÄVER:
            nytt_barn = nuvarande_ord[:i] + b + nuvarande_ord[i+1:]

            if nytt_barn in svenska and nytt_barn not in gamla:
                if nytt_barn == slutord:
                    print(f"\nHittade en väg från {startord} till {slutord}")
                    exit()

                gamla.append(nytt_barn)
                q.enqueue(nytt_barn)

startord = input("\nStartord: ")
slutord = input("Slutord: ")
if len(startord) != 3 or len(slutord) != 3:
    print("\nOrden måste vara tre tecken långt")
    exit()

q = LinkedQ()
q.enqueue(startord)
gamla = []
gamla.append(startord)
while not q.isEmpty():
    nuvarande = q.dequeue()
    makechildren(nuvarande)

print("\nHittade ingen väg")
