print ("Clase 26/09/2023")
loona_integrantes = []  


for nombre in ["HeeJin", "HyunJin", "HaSeul", "YeoJin", "ViVi", "Kim Lip", "JinSoul", "Choerry", "Yves", "Chuu", "Go Won", "Olivia Hye"]:
    loona_integrantes.append(nombre)

print(loona_integrantes)

gatito = [
    " /\_/\ ",
    "( o.o )",
    " > ^ < "
]


frase = "arriba Loona"

for i, linea in enumerate(gatito):
    if i == 0:
        print(frase.center(len(linea)))
    print(linea)