from linkedQFile import LinkedQ


kortlek = LinkedQ()
valda_kort = input("\nVilken ordning ligger korten i? ").split()

for kort in valda_kort:    
    kortlek.enqueue(str(kort))

slutordning = []
while not kortlek.isEmpty():
    flytta_bak = kortlek.dequeue()
    kortlek.enqueue(flytta_bak)
    ta_bort = kortlek.dequeue()
    slutordning.append(ta_bort)

print("\nKorten kommer ut i denna ordning: ", end="")
print(*slutordning, sep=" ")

