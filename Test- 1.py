nombre=input("Escriba su nombre")
largo=len(nombre)
print(nombre,largo)
i=largo
for i in range(largo,-1):
    print(nombre[i])

def espacio(n):
    return " " *3*n
Nombre = input("Escriba su nombre: ")
largo = len(Nombre)
for i in range(largo):
    if i == 0:
        print(Nombre[0])
    else:
        print(espacio(i) + Nombre[i])

def nombre_vertical():
    Nombre = input( "Escriba su nombre: ")
    largo = len(Nombre)
    for i in range(0, largo):
      print(Nombre[i] + "\n") 
for n in range(3):
    nombre_vertical()


