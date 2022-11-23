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


def satisfactionCalculatorB(b, couple):
    choice = b.index(couple[0])
    res = 100 - choice * (100 / (len(b) - 1))

    return res


def statisfactionInitializer(A):
    res = []
    i = len(A)
    while i > 0:
        i = i - 1
        res.append([])
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


def maxLen(liste):
    maximum = 0
    for L in liste:
        if maximum < len(L):
            maximum = len(L)

    return maximum


def meanSatisf(satisfA, satisfB):
    res1 = []
    res2 = []
    res = []
    maximum = max(maxLen(satisfA), maxLen(satisfB))
    for i in range(maximum):
        res1.append(0)
        for L in satisfA:
            if len(L) <= i:
                res1[i] += L[len(L) - 1]
            else:
                res1[i] += L[i]
        res1[i] /= len(satisfA)
    for i in range(maximum):
        res2.append(0)
        for L in satisfB:
            if len(L) <= i:
                res2[i] += L[len(L) - 1]
            else:
                res2[i] += L[i]
        res2[i] /= len(satisfB)
    res.append(res1)
    res.append(res2)
    return res


def GS(A, B, Pref):
    libreA = A
    libreB = B
    couple = []
    PrefCopy = copyList(Pref)
    satisfactionA = statisfactionInitializer(A)
    satisfactionB = statisfactionInitializer(B)
    while (libreA != []):
        a = libreA[0]
        b = Pref[0][a][0]
        if b in libreB:
            libreA.remove(a)
            libreB.remove(b)
            couple.append([a, b])
            satisfactionA[a].append(satisfactionCalculatorA(PrefCopy[0][a], [a, b]))
            satisfactionB[b].append(satisfactionCalculatorB(PrefCopy[0][a], [a, b]))
            # print("Couple" + str(couple))
        else:
            partnerB = findPartner(couple, b)
            if betterChoice(Pref[1][b], partnerB, a) == a:
                libreA.remove(a)
                libreA.append(partnerB)
                couple.remove([partnerB, b])
                couple.append([a, b])
                satisfactionA[a].append(satisfactionCalculatorA(PrefCopy[0][a], [a, b]))
                satisfactionB[b].append(satisfactionCalculatorB(PrefCopy[1][b], [a, b]))
                # print("Couple" + str(couple))
            else:
                Pref[0][a].remove(b)
                # print("Couple" + str(couple))

    return {"couple": couple, "satisfactionA": satisfactionA, "satisfactionB": satisfactionB}


def calculerEns(x):
    res = []
    for i in range(x):
        res.append(i)
    return res


dataset1 = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
dataset2 = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[2, 1, 0], [2, 1, 0], [2, 1, 0]]]
dataset3 = [[[0, 1, 2], [1, 2, 0], [2, 0, 1]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

# Pref = random_preference(TAILLE, TAILLE, TAILLE)
Pref = dataset3
Pref2 = copyList(Pref)
Pref2.reverse()
print(Pref)
print(Pref2)
A = calculerEns(TAILLE)
B = calculerEns(TAILLE)
A2 = calculerEns(TAILLE)
B2 = calculerEns(TAILLE)

resGSEtu = GS(A, B, Pref)
resGSEtab = GS(B2, A2, Pref2)
print(resGSEtu)
print(resGSEtab)


def plotSatisf(resGS, meanA, meanB, labelA, labelB):
    X = []
    for i in range(max(maxLen(resGS.get("satisfactionA")), maxLen(resGS.get("satisfactionB")))):
        X.append(i + 1)
    print(X)
    plt.plot(X, meanA, label=labelA)
    plt.plot(X, meanB, label=labelB)
    plt.xlabel('n-eme affectation')
    plt.ylabel('Moyenne de satisfaction de tous les éléments d\'un groupe,\n en pourcentage')
    plt.title('Satisfaction à chaque affectation')
    plt.legend()
    # plt.ylim(0, 100)
    plt.xticks(X)
    plt.show()


meanEtu = meanSatisf(resGSEtu.get("satisfactionA"), resGSEtu.get("satisfactionB"))
meanAEtu = meanEtu[0]
meanBEtu = meanEtu[1]
print("moyennes pref A" + str(meanAEtu))
print("moyennes pref B" + str(meanBEtu))
plotSatisf(resGSEtu, meanAEtu, meanBEtu, "Étudiants", "Établissements")

meanEtab = meanSatisf(resGSEtab.get("satisfactionA"), resGSEtab.get("satisfactionB"))
meanAEtab = meanEtab[0]
meanBEtab = meanEtab[1]
print("moyennes pref A" + str(meanAEtab))
print("moyennes pref B" + str(meanBEtab))
plotSatisf(resGSEtab, meanAEtab, meanBEtab, "Établissements", "Étudiants")
