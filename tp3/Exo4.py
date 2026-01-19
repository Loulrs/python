def trouver_maximum(a, b, c):
    """Renvoie le plus grand des trois nombres (a, b, c)."""

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    nombre1 = 15
    nombre2 = 28
    nombre3 = 10
 
    resultat_max = trouver_maximum(nombre1, nombre2, nombre3)

    print(f"Les nombres sont : {nombre1}, {nombre2}, {nombre3}")
    print(f"Le maximum est : {resultat_max}")
