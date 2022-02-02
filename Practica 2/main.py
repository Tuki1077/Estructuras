import functions as function
#Programa para creditos y debitos
#Arrays unidimensionales


contador = 0
#Llenamos el array de creditos
n = int(input('Ingrese la cantidad de creditos que desea agregar (Minimo 5!): '))
if n >= 5:
    print('Ingrese sus valores:')
    for i in range(0, n):
        val_creditos = input()
        if function.agregar_credito(val_creditos) == False:
            print ("Valor no es valido!")

#Llenamos el array de debitos
n1 = int(input('Ingrese la cantidad de debitos que desea agregar (Minimo 10!): '))
if n1 >= 10:
    print ('Ingrese sus valores: ')
    for i in range (0,n1):
        val_debitos = input ()
        if function.agregar_debito(val_debitos) == False:
            print ("Valor no es valido")

while (True):
    print ("------------------------------")
    opcion = int (input ('Ingrese una opcion: \n 1. Total de Creditos \n 2. Total de Debitos \n 3. Saldo \n 4. Promedio de debitos \n 5. Mostrar Debito mas grande \n 6. Eliminar creditos \n 7. Exit \n'))
    print ("------------------------------")

    if opcion == 1:
        function.total_creditos()
        print ("La suma total de creditos es: ", function.total_creditos())
        contador = contador + 1
    elif opcion == 2:
        function.total_debitos()
        print ("La suma total de debitos es: ", function.total_debitos())
        contador = contador + 1
    elif opcion == 3:
        function.saldo()
        print ("Su saldo total: ", function.saldo())
        contador = contador + 1
    elif opcion == 4:
        function.avrg_debitos()
        contador = contador + 1
    elif opcion == 5:
        function.debito_mayor()
        contador = contador + 1
    elif opcion == 6:
        function.eliminar_credito()
        contador = contador + 1
    elif opcion == 7:
        print ("La cantidad de ejecuciones fue de: ", contador)
        print (quit)
        quit()
            


