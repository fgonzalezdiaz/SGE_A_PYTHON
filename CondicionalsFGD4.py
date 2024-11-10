salari = int(input("Quin es el teu salari?: "))
if salari <= 15000:
    salarinet = 15000
elif salari <= 30000:
    salarinet = salari - (salari * 0.10)
elif salari <= 60000:
    salarinet = salari - (salari * 0.21)
else :
    salarinet = salari - (salari * 0.50)
print (f"El teu salari net es de {salarinet}")