notes_texte = input("Entrez les notes, séparées par un espace (ex: 12 15.5 18) : ")

liste_notes = notes_texte.split()

somme = 0
nombre_notes = 0

for note_str in liste_notes:
    try:
        note_num = float(note_str)
        somme += note_num
        nombre_notes += 1
    except ValueError:
        print(f"Attention : '{note_str}' n'est pas une note valide et sera ignorée.")

if nombre_notes > 0:
    moyenne = somme / nombre_notes
    print("-" * 20)
    print(f"Nombre de notes prises en compte : {nombre_notes}")
    print(f"Somme totale des notes : {somme}")
    print(f"La MOYENNE des notes est : {moyenne:.2f}") 
else:
    print("La liste de notes est vide. Impossible de calculer la moyenne.")