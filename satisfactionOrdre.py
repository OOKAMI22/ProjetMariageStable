import random
import matplotlib.pyplot as plt

TAILLE = 3


def random_preference(nbEtu, nbEcole, nbPref):
    res = [[], []]
    for i in range(nbEtu):
        # res.append([i,i])
        res[0].append(random.sample(range(0, nbEcole), nbPref))
    for i in range(nbEcole):
        res[1].append(random.sample(range(0, nbEtu), nbPref))
    return res


def findPartner(couples, x):
    for couple in couples:
        if couple[1] == x:
            return couple[0]
    return None


def betterChoice(choices, x, y):
    for choice in choices:
        if choice == x:
            return x
        if choice == y:
            return y
    return None


def satisfactionCalculatorA(a, couple):
    choice = a.index(couple[1])
    res = 100 - choice * (100 / (len(a) - 1))

    return res


def copyList(liste):
    copy = []
    for i in range(len(liste)):
        copy.append([])
        for j in range(len(liste[i])):
            copy[i].append([])
            for k in range(len(liste[i][j])):
                copy[i][j].append(liste[i][j][k])
    return copy


def classement(n):
    tab = []
    used = []

    for i in range(n):
        y = True
        while (y):
            x = random.randint(0, n - 1)
            if (x not in used):
                tab.append(x)
                y = False

        used.append(x)
    return tab


def GS(A, B, Pref, classement):
    libreA = A
    libreB = B
    couple = []
    PrefCopy = copyList(Pref)

    while (libreA != []):
        a = libreA[0]
        b = Pref[0][a][0]
        if b in libreB:
            libreA.remove(a)
            libreB.remove(b)
            couple.append([a, b])

            # print("Couple" + str(couple))
        else:
            partnerB = findPartner(couple, b)
            if betterChoice(Pref[1][b], partnerB, a) == a:
                libreA.remove(a)
                libreA.append(partnerB)
                couple.remove([partnerB, b])
                couple.append([a, b])

                # print("Couple" + str(couple))
            else:
                Pref[0][a].remove(b)
                # print("Couple" + str(couple))

    return couple


def calculerEns(x):
    res = []
    for i in range(x):
        res.append(i)
    return res


def findCouple(couples, x):
    for couple in couples:
        if x in couple:
            return couple
    return []


def calculSatisf(pref, couples, ordre, priorite):
    nbMajor = int(0.1 * len(ordre)) + 1
    res = 0
    for x in range(nbMajor):
        couple = findCouple(couples, ordre[x])
        if priorite == "etu":
            a = pref[0][ordre[x]]
            choice = a.index(couple[1])
        else:
            a = pref[1][ordre[x]]
            choice = a.index(couple[0])
        res = 100 - choice * (100 / (len(a) - 1))
    return res


dataset1 = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
dataset2 = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[2, 1, 0], [2, 1, 0], [2, 1, 0]]]
dataset3 = [[[0, 1, 2], [1, 2, 0], [2, 0, 1]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
dataset4 = [[[0, 1, 2], [1, 0, 2], [2, 1, 0]], [[0, 1, 2], [2, 1, 0], [1, 2, 0]]]

# Pref = random_preference(TAILLE, TAILLE, TAILLE)
Pref = dataset1
Pref2 = copyList(Pref)
Pref2.reverse()
ordre = classement(TAILLE)
print("classement des étudiants : ", ordre)
print(Pref)
print(Pref2)
A = calculerEns(TAILLE)
B = calculerEns(TAILLE)
A2 = calculerEns(TAILLE)
B2 = calculerEns(TAILLE)

resGSEtu = GS(A, B, Pref, ordre)
resGSEtab = GS(B2, A2, Pref2, ordre)
print(resGSEtu)
print(resGSEtab)
print("satisfaction selon les majors priorité etu : ", calculSatisf(Pref, resGSEtab, ordre, "etu"))
print("satisfaction selon les majors priorité etab : ", calculSatisf(Pref2, resGSEtab, ordre, "etab"))
