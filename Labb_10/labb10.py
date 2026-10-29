from linkedQFile import LinkedQ
from molgrafik import *

class Syntaxfel(Exception):
    pass

siffror = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

storabokstäver = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]

bokstäver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]


atomdata = "H  1.00794;\
            He 4.002602;\
            Li 6.941;\
            Be 9.012182;\
            B  10.811;\
            C  12.0107;\
            N  14.0067;\
            O  15.9994;\
            F  18.9984032;\
            Ne 20.1797;\
            Na 22.98976928;\
            Mg 24.3050;\
            Al 26.9815386;\
            Si 28.0855;\
            P  30.973762;\
            S  32.065;\
            Cl 35.453;\
            K  39.0983;\
            Ar 39.948;\
            Ca 40.078;\
            Sc 44.955912;\
            Ti 47.867;\
            V  50.9415;\
            Cr 51.9961;\
            Mn 54.938045;\
            Fe 55.845;\
            Ni 58.6934;\
            Co 58.933195;\
            Cu 63.546;\
            Zn 65.38;\
            Ga 69.723;\
            Ge 72.64;\
            As 74.92160;\
            Se 78.96;\
            Br 79.904;\
            Kr 83.798;\
            Rb 85.4678;\
            Sr 87.62;\
            Y  88.90585;\
            Zr 91.224;\
            Nb 92.90638;\
            Mo 95.96;\
            Tc 98;\
            Ru 101.07;\
            Rh 102.90550;\
            Pd 106.42;\
            Ag 107.8682;\
            Cd 112.411;\
            In 114.818;\
            Sn 118.710;\
            Sb 121.760;\
            I  126.90447;\
            Te 127.60;\
            Xe 131.293;\
            Cs 132.9054519;\
            Ba 137.327;\
            La 138.90547;\
            Ce 140.116;\
            Pr 140.90765;\
            Nd 144.242;\
            Pm 145;\
            Sm 150.36;\
            Eu 151.964;\
            Gd 157.25;\
            Tb 158.92535;\
            Dy 162.500;\
            Ho 164.93032;\
            Er 167.259;\
            Tm 168.93421;\
            Yb 173.054;\
            Lu 174.9668;\
            Hf 178.49;\
            Ta 180.94788;\
            W  183.84;\
            Re 186.207;\
            Os 190.23;\
            Ir 192.217;\
            Pt 195.084;\
            Au 196.966569;\
            Hg 200.59;\
            Tl 204.3833;\
            Pb 207.2;\
            Bi 208.98040;\
            Po 209;\
            At 210;\
            Rn 222;\
            Fr 223;\
            Ra 226;\
            Ac 227;\
            Pa 231.03588;\
            Th 232.03806;\
            Np 237;\
            U  238.02891;\
            Am 243;\
            Pu 244;\
            Cm 247;\
            Bk 247;\
            Cf 251;\
            Es 252;\
            Fm 257;\
            Md 258;\
            No 259;\
            Lr 262;\
            Rf 265;\
            Db 268;\
            Hs 270;\
            Sg 271;\
            Bh 272;\
            Mt 276;\
            Rg 280;\
            Ds 281;\
            Cn 285"

atomlista = {}
lista = atomdata.split(";")
for namn_vikt in lista:
    namn, vikt = namn_vikt.split()
    atomlista[namn] = float(vikt)


def readformel(q):
    mol = readmol(q)
    return mol

def readmol(q):
    mol = readgroup(q)
    n = q.peek()
    if n is not None and n != ")":
        mol.next = readmol(q)
    return mol

def readgroup(q):
    rutan = Ruta()

    n = q.peek()

    if n == "(":
        q.dequeue()
        rutan.down = readmol(q)
        n = q.dequeue()
        if n != ")":
            raise Syntaxfel(f"Saknad högerparentes vid radslutet {q}")
        if q.peek() in siffror:
            readnum(q, rutan)
        else:
            raise Syntaxfel(f"Saknad siffra vid radslutet {q}")
    else:
        readatom(q, rutan)
        if not q.isEmpty() and q.peek() in siffror:
            readnum(q, rutan)
    return rutan

def readatom(q, rutan):
    readLETTER(q)
    första = q.dequeue()

    atomen = LinkedQ()
    atomen.enqueue(första)

    if q.peek() in bokstäver:
        readletter(q)
        andra = q.dequeue()
        atomen.enqueue(andra)

    if str(atomen) not in atomlista:
        raise Syntaxfel(f"Okänd atom vid radslutet {q}")
    rutan.atom = str(atomen)

def readLETTER(q):
    n = q.peek()
    if n in storabokstäver:
        return
    if n in bokstäver:
        raise Syntaxfel(f"Saknad stor bokstav vid radslutet {q}")
    raise Syntaxfel(f"Felaktig gruppstart vid radslutet {q}")


def readletter(q):
    n = q.peek()
    if n is None:
        return
    if n in bokstäver:
        return
    raise Syntaxfel(f"Felaktig bokstav vid radslutet {q}")


def readnum(q, rutan):
    n = q.peek()
    if n == "0":
        q.dequeue()
        raise Syntaxfel(f"För litet tal vid radslutet {q}")

    nummer = LinkedQ()

    if n == "1":
        q.dequeue()
        nummer.enqueue(n)
        n = q.peek()
        if n not in siffror:
            raise Syntaxfel(f"För litet tal vid radslutet {q}")

    while True:
        n = q.peek()
        if n not in siffror:
            rutan.num = int(str(nummer))
            return
        n = q.dequeue()
        nummer.enqueue(n)


def kontrollera_readformel(inmatning):
    q = LinkedQ()
    for tkn in inmatning:
        q.enqueue(tkn)


    try:
        mol = readformel(q)
        if not q.isEmpty():
            raise Syntaxfel(f"Felaktig gruppstart vid radslutet {q}")
        return "Formeln är syntaktiskt korrekt", mol
    except Syntaxfel as fel:
        return str(fel), None

def weightatom(ruta):
    if ruta.down is None:
        return atomlista[ruta.atom] * ruta.num
    else:
        return weightmol(ruta.down) * ruta.num

def weightmol(mol):
    weight = weightatom(mol)

    if mol.next is not None:
        weight += weightmol(mol.next)

    return weight


def main():
    mg = Molgrafik()

    while True:
        inmatning = input()
        if inmatning == "#":
            break
        else:
            resultat, mol = kontrollera_readformel(inmatning)
            if mol is not None:
                print(weightmol(mol))
                print(resultat)
                mg.show(mol)
                mg.root.mainloop()

            else:
                print(resultat)



if __name__ == "__main__":
    main()
