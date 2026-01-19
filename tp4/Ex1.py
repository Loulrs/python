import pandas as pandasLib

dataFrame1MonJeuDeDonneeDentrainement = pandasLib.read_csv("donnevrai.csv")

dataFrame1MonJeuDeDonneeDentrainement["danger"] = dataFrame1MonJeuDeDonneeDentrainement["danger"].map({"safe": 0, "danger": 1})

X = dataFrame1MonJeuDeDonneeDentrainement["vitesse"].tolist()
Y = dataFrame1MonJeuDeDonneeDentrainement["danger"].tolist()

print("Données X (vitesses):", X[:5])
print("Données Y (dangers):", Y[:5])

import random

w = random.randint(-10, 10)
b = random.randint(-10, 10)

print(f"Valeurs initiales : w = {w}, b = {b}")

def Zpredict(x):
    Z = w * x + b
    if Z >= 0:
        return 1
    else:
        return 0
    
    print("\nTest de prédiction:")
for x in X[:5]:
    print(f"x = {x}, prédiction = {Zpredict(x)}")

    print("\nCalcul des erreurs:")
for x, y in zip(X, Y):
    y_pred = Zpredict(x)
    erreur = y - y_pred
    print(f"x = {x}, y_attendu = {y}, y_prédit = {y_pred}, erreur = {erreur}")