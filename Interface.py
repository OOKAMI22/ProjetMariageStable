import random
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QLineEdit

widgets = {"logo": [],
           "button": [],
           "etudiant": [],
           "etablissement": [],
           "preference": [],
           "preferences": [],
           "couples":[],
           "answer1": []}

neededInformations = {"nbEtu": 0, "nbEtab": 0, "nbPref": 0, "preferences": []}
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Projet Mariage Stable")
window.setFixedWidth(1000)
window.move(2700, 200)
window.setStyleSheet("background: #161219;")
grid = QGridLayout()


def random_preference(nbEtu, nbEcole, nbPref):
    res = [[], []]
    for i in range(nbEtu):
        # res.append([i,i])
        res[0].append(random.sample(range(0, nbEcole), nbPref))
    for i in range(nbEtu):
        res[1].append(random.sample(range(0, nbEtu), nbPref))
    return res


def affichage(preference):
    res = "Les preferences calculées aléatoirement sont : \n Pour les étudiants : \n"
    for i in range(len(preference[0])):
        res += "etu" + str(i) + " : " + str(preference[0][i]) + "\n"
    res += "Pour les établissements : \n"
    for i in range(len(preference[1])):
        res += "etab" + str(i) + " : " + str(preference[1][i]) + "\n"

    return res

def calculerEns(x):
  res = []
  for i in range(x):
    res.append(i)
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

def affichage_couples(couples):
  res = "Les couples stables (etu,etab) calculés avec l'algorithme GS sont : \n"
  for couple in couples:
    res += str(couple)+"\n"
  return res

def create_buttons(name):
    button = QPushButton(name)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                         "border-radius: 25px;" +
                         "font-family:'shanti';" +
                         "font-size: 35px;" +
                         "color: 'white';" +
                         "padding: 25px 0;" +
                         "margin-top: 30px;}" +
                         "*:hover{background: '#BC006C';}")

    return button


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
            if len(widgets[widget]) > 1:
                widgets[widget][-2].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def start():
    clear_widgets()
    formulaireFrame()


def acceuilFrame():
    # Afficher le logo
    image = QPixmap("um.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    # Button widget
    button = QPushButton("Let's start")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                         "border-radius: 45px;" +
                         "font-size: 35px;" +
                         "color: 'white';" +
                         "padding: 25px 0;" +
                         "margin: 100px 200px;}" +
                         "*:hover{background: '#BC006C';}")
    button.clicked.connect(start)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)


def formulaireFrame():
    clear_widgets()
    etudiant = QLabel("Nombre d'étudiant")
    etudiant.setAlignment(QtCore.Qt.AlignCenter)
    etudiant.setWordWrap(True)
    etudiant.setStyleSheet("font-family: Shanti;"
                           "font-size: 25px;" +
                           "color: 'white';" +
                           "padding: 75px;")
    widgets["etudiant"].append(etudiant)
    etudiantInput = QLineEdit()
    etudiantInput.setStyleSheet("border: 4px solid '#BC006C';" +
                                "border-radius: 45px;" +
                                "font-family: Shanti;"
                                "color: 'white';" +
                                "padding: 25px;")
    etudiantInput.move(80, 20)
    etudiantInput.resize(200, 32)
    etudiantInput.setAlignment(QtCore.Qt.AlignCenter)
    widgets["etudiant"].append(etudiantInput)
    grid.addWidget(widgets["etudiant"][-1], 1, 0, 1, 0)
    grid.addWidget(widgets["etudiant"][-2], 1, 0, 1, 1)

    etab = QLabel("Nombre d'établissement")
    etab.setAlignment(QtCore.Qt.AlignCenter)
    etab.setWordWrap(True)
    etab.setStyleSheet("font-family: Shanti;"
                       "font-size: 25px;" +
                       "color: 'white';" +
                       "padding: 75px;")
    widgets["etablissement"].append(etab)
    etabInput = QLineEdit()
    etabInput.setStyleSheet("border: 4px solid '#BC006C';" +
                            "border-radius: 45px;" +
                            "font-family: Shanti;"
                            "color: 'white';" +
                            "padding: 25px;")
    etabInput.move(80, 20)
    etabInput.resize(200, 32)
    etabInput.setAlignment(QtCore.Qt.AlignCenter)
    widgets["etablissement"].append(etabInput)
    grid.addWidget(widgets["etablissement"][-1], 0, 0, 1, 0)
    grid.addWidget(widgets["etablissement"][-2], 0, 0, 1, 1)

    pref = QLabel("Entrez le nombre de preference")
    pref.setAlignment(QtCore.Qt.AlignCenter)
    pref.setWordWrap(True)
    pref.setStyleSheet("font-family: Shanti;"
                       "font-size: 25px;" +
                       "color: 'white';" +
                       "padding: 75px;")
    widgets["preference"].append(pref)
    prefInput = QLineEdit()
    prefInput.setStyleSheet("border: 4px solid '#BC006C';" +
                            "border-radius: 45px;" +
                            "font-family: Shanti;"
                            "color: 'white';" +
                            "padding: 25px;")
    prefInput.move(80, 20)
    prefInput.resize(200, 32)
    prefInput.setAlignment(QtCore.Qt.AlignCenter)
    widgets["preference"].append(prefInput)
    grid.addWidget(widgets["preference"][-1], 2, 0, 1, 0)
    grid.addWidget(widgets["preference"][-2], 2, 0, 1, 1)

    button = create_buttons("Next")
    button.clicked.connect(calcul)
    # button.setAlignment(QtCore.Qt.AlignCenter)
    widgets["answer1"].append(button)
    grid.addWidget(widgets["answer1"][-1], 3, 1)


def calcul():
    neededInformations["nbEtu"] = int(widgets["etudiant"][-1].text())
    neededInformations["nbEtab"] = int(widgets["preference"][-1].text())
    neededInformations["nbPref"] = int(widgets["etablissement"][-1].text())
    neededInformations["preferences"] = random_preference(neededInformations["nbEtu"], neededInformations["nbEtab"],
                                                          neededInformations["nbPref"])
    print(neededInformations)
    clear_widgets()
    pref = QLabel(affichage(neededInformations["preferences"]))
    pref.setAlignment(QtCore.Qt.AlignCenter)
    pref.setWordWrap(True)
    pref.setStyleSheet("font-family: Shanti;"
                           "font-size: 25px;" +
                           "color: 'white';" +
                           "padding: 75px;")
    widgets["preferences"].append(pref)
    grid.addWidget(widgets["preferences"][-1], 1, 0, 1, 0)
    button = create_buttons("calculer les couples stables")
    button.clicked.connect(GSFrame)
    # button.setAlignment(QtCore.Qt.AlignCenter)
    widgets["answer1"].append(button)
    grid.addWidget(widgets["answer1"][-1], 3, 1)
    #afficheCalculFrame()


def GSFrame():
    clear_widgets()
    A = calculerEns(neededInformations["nbEtu"])
    B = calculerEns(neededInformations["nbEtab"])
    print(A)
    print(B)
    couples = GS(A,B,neededInformations["preferences"])
    print(couples)
    CS = QLabel(affichage_couples(couples))
    CS.setAlignment(QtCore.Qt.AlignCenter)
    CS.setWordWrap(True)
    CS.setStyleSheet("font-family: Shanti;"
                       "font-size: 25px;" +
                       "color: 'white';" +
                       "padding: 75px;")
    widgets["couples"].append(CS)
    grid.addWidget(widgets["couples"][-1], 1, 0, 1, 0)
    button = create_buttons("relancer")
    button.clicked.connect(formulaireFrame)
    # button.setAlignment(QtCore.Qt.AlignCenter)
    widgets["answer1"].append(button)
    grid.addWidget(widgets["answer1"][-1], 3, 1)


acceuilFrame()

window.setLayout(grid)

window.show()

sys.exit(app.exec())
