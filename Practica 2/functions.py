creditos = []
debitos = []

def agregar_credito(credito):
    try: 
        credit = float(credito)
        creditos.append(credit)
        return True
    except:
        return False

def total_creditos():
    #Encontramos la suma total de los creditos usando "sum"
    #print ("Sus creditos son: ")
    #print (creditos)
    if len(creditos) > 0:
        suma = sum(creditos)
        return suma
    else:
        return 0

def total_debitos ():
    #Encontramos la suma total de debitos usando "sum"
    print ("Sus debitos son:")
    print(debitos)
    suma_debitos = sum(debitos)
    print ("La suma total de debitos es: ", suma_debitos)

def saldo():
    #Saldo total es debitos-creditos
    suma_debitos = sum (debitos)
    suma_creditos = sum (creditos)    
    saldo = suma_debitos - suma_creditos
    print("Su saldo actual es: ", saldo)

def avrg_debitos():
    #Promedio es igual a la suma de los debitos / la cantidad de datos que se encuentran en el array
    promedio = sum (debitos) / len (debitos)
    print ("El promedio de debitos es", promedio)


def debito_mayor():
    #Primera hacemos sort el array de mas chico a mas grande
    debitos.sort()
    largest_element = debitos[0]
    #Recorremos el array para encontrar el dato mas grande del array
    for i in range (0, len(debitos)):
        if (debitos[i] > largest_element):
            largest_element = debitos [i]
    
    print ("El debito mas grande es: ", largest_element)

def eliminar_credito():
    print ("Sus creditos actuales son:", creditos, "\n")
    eliminar = int(input ("Indique segun la posicion, cual desea eliminar \n"))
    eliminar = eliminar - 1
    creditos.pop(eliminar)
    print ("Sus nuevos creditos son: ", creditos)
