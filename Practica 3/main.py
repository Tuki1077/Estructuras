import functions as func
from typing import NamedTuple

class Struct(NamedTuple):
    quadrant: str


print ("Ingrese dos valores para poder determinar si el cuadrante en el que se encuentra!")
X = float(input("Porfavor ingrese su primera valor: "))
Y = float(input("Porfavor ingrese su segundo valor: "))

my_value = Struct(func.quadrant(X,Y))


print (my_value)
