nombre=input("Escriba su nombre")
largo=len(nombre)
print(nombre,largo)
i=largo
for i in range(largo,-1):
    print(nombre[i])
