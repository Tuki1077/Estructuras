#Programa para creditos y debitos
#Arrays unidimensionales

creditos = []
debitos = []

def agregar_credito(credito):
    try: 
        float(credito)
        creditos.append(credito)
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




def main ():
    contador = 0
    #Llenamos el array de creditos
    n = int(input('Ingrese la cantidad de creditos que desea agregar (Minimo 5!): '))
    if n >= 5:
        print('Ingrese sus valores:')
        for i in range(0, n):
            val_creditos = input()
            if agregar_credito(val_creditos) == False:
                print ("Valor no es valido!")

    #Llenamos el array de debitos
    n1 = int(input('Ingrese la cantidad de debitos que desea agregar (Minimo 10!): '))
    if n1 >= 10:
        print ('Ingrese sus valores: ')
        for i in range (0,n1):
            val_debitos = int(input ())
            debitos.append(val_debitos)

    while (True):
        print ("------------------------------")
        opcion = int (input ('Ingrese una opcion: \n 1. Total de Creditos \n 2. Total de Debitos \n 3. Saldo \n 4. Promedio de debitos \n 5. Mostrar Debito mas grande \n 6. Eliminar creditos \n 7. Exit \n'))
        print ("------------------------------")

        if opcion == 1:
            total_creditos()
            contador = contador + 1
        elif opcion == 2:
            total_debitos()
        elif opcion == 3:
            saldo()
        elif opcion == 4:
            avrg_debitos()
        elif opcion == 5:
            debito_mayor()
        elif opcion == 6:
            eliminar_credito()
        elif opcion == 7:
            print (quit)
            quit()
            


main()