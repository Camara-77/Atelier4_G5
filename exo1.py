def calcul_somme(nombre1,nombre2):
    return nombre1 + nombre2

nombreSai1=(input("veuillez donner deux nombres "))
nombreSai2=(input("veuillez donner deux nombres "))
# while nombreSai1 < 0 or nombreSai2 < 0:
while  not nombreSai1.replace('.','').isdigit() or not nombreSai2.replace('.','').isdigit():
    print("ce que vous avez saisi c'est pas un nombre ")
    nombreSai1=(input("veuillez redonner deux nombres "))
    nombreSai2=(input("veuillez redonner deux nombres "))

nombreSai1 =float(nombreSai1)
nombreSai2 =float(nombreSai2)
print(calcul_somme(nombreSai1,nombreSai2))