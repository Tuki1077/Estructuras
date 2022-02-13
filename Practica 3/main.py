import functions as func

print ("Ingrese dos valores para poder determinar si el cuadrante en el que se encuentra!")
X = float(input("Porfavor ingrese su primera valor: \n"))
Y = float(input("Porfavor ingrese su segundo valor: \n"))

Quadrant = func.quadrant(X, Y)

print (Quadrant)
