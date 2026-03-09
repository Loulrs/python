import random


X = [50, 70, 85, 100, 40, 110, 75, 95]
Y = [0,  0,  1,  1,   0,  1,   0,  1]

def predict(x, w, b):
    z = x * w + b
    return 1 if z >= 0 else 0

w = random.uniform(-10, 10)
b = random.uniform(-10, 10)

eta = 0.001      
epochs = 5000   

print(f"Départ: w={w:.2f}, b={b:.2f}")

for epoch in range(epochs):
    erreurs = 0
    for x, y in zip(X, Y):
        y_pred = predict(x, w, b) 
        erreur = y - y_pred       
        
        if erreur != 0:
            w += eta * erreur * x  
            b += eta * erreur      
            erreurs += 1           
    
    if erreurs == 0:
        print(f"Apprentissage terminé à l'époque {epoch+1}.") 
        break

print("\n--- Vérification finale ---")
print("Prédictions après entraînement :")

for x in X:
    res = "Danger" if predict(x, w, b) == 1 else "Safe"
    print(f"vitesse = {x} km/h -> {res}")


print("\n--- Testeur de Vitesse (Exercice 3) ---")
print("Le neurone est prêt. Entrez des vitesses pour tester.")

while True:
    saisie = input("\nEntrez une vitesse (ou 'stop' pour quitter) : ")
    
    if saisie.lower() == 'stop':
        break
    
    try:
        vitesse_test = float(saisie)
        resultat = predict(vitesse_test, w, b)
        
        if resultat == 1:
            print(f" Vitesse : {vitesse_test} km/h -> DANGER !")
        else:
            print(f" Vitesse : {vitesse_test} km/h -> Safe.")
            
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")