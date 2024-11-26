#Mostrarem números de l'1 al 10 amb un for
for i in [1,2,3,4,5,6,7,8,9,10]:
    print (f"Comptador amb for {i}")

#Mostrarem números de l'1 al 10 amb un while
k = 1
while k <= 10:
    print (f"Comptador amb while {k}")
    k = k + 1

#Imprimirem els elementr d'una llista amb for
fruits=["poma", "pera", "raïm", "plàtan"]

for j in fruits:
    print (f"Fruites {j}")

#Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
for l in num:
    if l % 2 == 0:
        print(f"Es parell:  {l}")

#Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.
suma = 0
for m in num:
    if m % 2 == 0:
        suma = suma + m

print (f"Suma dels caracters parells {suma}")

#Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.
m = 0
while m <= 100:
    print (f"Contador {m}")
    m = m + 1

#Amb while indicar si el número guardat a una variable està entre 100 i 400.
dinsInt = int(input(f"Escriu un numero: "))
contador = 0
while contador <= 400:
    if contador == dinsInt :
        if contador >= 100:
            print(f"{dinsInt} es una variable dins el rang 100 i 400")
    contador = contador + 1

