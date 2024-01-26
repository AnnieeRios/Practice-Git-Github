
menuOp1 = input("Ingresa 'si' para ver opciones o 'no' para cerrar: ")
if menuOp1 == "si":
  print("""Que quisieras realizar, ingrese el numero de acuerdo a la opción:
  1) Añadir un nuevo estudiante 
  2) Ver la lista de estudiantes 
  3) Eliminar el archivo """)
  menuOp2 = input("Ingrese una de las opciones")

if menuOp2 == "1":
  stdFile = open("filename", "a")
  fName = input ("Ingrese el nombre")
  LName = input ("Ingrese el apellido")
  Age = input("Ingrese una edad")
  student = "\n {} {} {}".format(fName, LName, Age)
  
elif menuOp2 == "2":
  
  pass