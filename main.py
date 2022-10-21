import random
def random_preference(nbEtu,nbEcole,nbPref):
  res = [[],[]]
  for i in range(nbEtu):
    #res.append([i,i])
    res[0].append(random.sample(range(0,nbEcole),nbPref))
  for i in range(nbEtu):
    res[1].append(random.sample(range(0,nbEtu),nbPref))
  return res

def findPartner(couples,x):
    for couple in couples:
        if couple[1] == x:
            return couple[0]
    return None
def betterChoice(choices,x,y):
  for choice in choices :
    if choice == x:
      return x
    if choice == y:
      return y
  return None


def GS(A,B,Pref):
  libreA = A
  libreB = B
  couple = []
  while(libreA != []):
    a = libreA[0]
    b = Pref[0][a][0]
    if b in libreB:
      libreA.remove(a)
      libreB.remove(b)
      couple.append([a,b])
    else:
        partnerB = findPartner(couple,b)
        if betterChoice(Pref[1][b],partnerB,a) == a:
            libreA.remove(a)
            libreA.append(partnerB)
            couple.remove([partnerB,b])
            couple.append([a,b])
        else:
            Pref[0][a].remove(b)


  return couple


Pref = random_preference(3,3,3)
print(Pref)
A = [0,1,2]
B = [0,1,2]
print(GS(A,B,Pref))

print(random_preference(3,3,3))