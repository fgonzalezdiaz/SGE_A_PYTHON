nota = int(input("Quina nota tens? "))

if nota <= 4.99 :
    nota2 = "S-Suspès"
elif nota <= 6.5 :
    nota2 = "A-Aprovat"
elif nota <= 8:
    nota2 = "N-Notable"
elif nota > 8 :
    nota2 = "E-Excel·lent"
print (nota2)