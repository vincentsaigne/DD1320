from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

siffror = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

storabokstäver = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]

bokstäver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

def group(inmatning):
    q = LinkedQ()
    for tkn in inmatning:
        q.enqueue(tkn)
    try:
        atom(q)
        num(q)
        print("Formeln är syntaktiskt korrekt")
    except Syntaxfel as fel:
        print(fel)

def atom(q):
    LETTER(q)
    q.dequeue()

    if q.peek() not in siffror:
        letter(q)
        q.dequeue()

def LETTER(q):
    n = q.peek()
    if n in storabokstäver:
        pass
    else:
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {q}")


def letter(q):
    n = q.peek()
    if n is None:
        pass
    elif n in bokstäver:
        pass
    else:
        raise Syntaxfel(f"Felaktig bokstav vid radslutet {q}")


def num(q):
    n = q.dequeue()
    if n == "0":
        raise Syntaxfel(f"För litet tal vid radslutet {q}")
    elif n == "1":
        n = q.peek()
        if n is None:
            raise Syntaxfel(f"För litet tal vid radslutet {q}")

    while True:
        if n is None:
            break
        if n not in siffror:
            raise Syntaxfel(f"Nummer får endast innehålla siffror {q}")
        n = q.dequeue()

def main():
    while True:
        inmatning = input()
        if inmatning == "#":
            break
        else:
            group(inmatning)

if __name__ == "__main__":
    main()
