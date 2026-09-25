def binary_search(lista, mal):
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

def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()