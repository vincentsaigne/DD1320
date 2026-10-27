from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

siffror = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

storabokstäver = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]

bokstäver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

atomer = "H  He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr\
        Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd\
        In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf\
        Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm\
        Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv".split()

def formel(q):
    mol(q)


def mol(q):
    group(q)
    n = q.peek()
    if n is not None and n != ")":
        mol(q)

def group(q):
    n = q.peek()

    if n == "(":
        q.dequeue()
        mol(q)
        n = q.dequeue()
        if n != ")":
            raise Syntaxfel(f"Saknad högerparentes vid radslutet {q}")
        if q.peek() in siffror:
            num(q)
        else:
            raise Syntaxfel(f"Saknad siffra vid radslutet {q}")
    else:
        atom(q)
        if not q.isEmpty():
            num(q)

def atom(q):
    LETTER(q)
    första = q.dequeue()

    atomen = LinkedQ()
    atomen.enqueue(första)

    if q.peek() in bokstäver:
        letter(q)
        andra = q.dequeue()
        atomen.enqueue(andra)

    if str(atomen) not in atomer:
        raise Syntaxfel(f"Okänd atom vid radslutet {q}")

def LETTER(q):
    n = q.peek()
    if n in storabokstäver:
        return
    if n in bokstäver:
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {q}")    
    raise Syntaxfel(f"Felaktig gruppstart vid radslutet {q}")


def letter(q):
    n = q.peek()
    if n is None:
        return
    if n in bokstäver:
        return
    raise Syntaxfel(f"Felaktig bokstav vid radslutet {q}")


def num(q):
    n = q.peek()
    if n == "0":
        q.dequeue()
        raise Syntaxfel(f"För litet tal vid radslutet {q}")
    if n == "1":
        q.dequeue()
        n = q.peek()
        if n not in siffror:
            raise Syntaxfel(f"För litet tal vid radslutet {q}")

    while True:
        n = q.peek()
        if n not in siffror:
            return
        n = q.dequeue()


def kontrollera_formel(inmatning):
    q = LinkedQ()
    for tkn in inmatning:
        q.enqueue(tkn)

    try:
        formel(q)
        if not q.isEmpty():
            raise Syntaxfel(f"Felaktig gruppstart vid radslutet {q}")
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)


def main():
    while True:
        inmatning = input()
        if inmatning == "#":
            break
        else:
            resultat = kontrollera_formel(inmatning)
            print(resultat)



if __name__ == "__main__":
    main()
