Diccionario ={}                   #Declaracion de diccionario vacio
while 1 :                         #While en este caso usado como loop infinito
    llave = input('Dame la clave del nuevo apartado del diccionario\n')      #Decalaracion de variable y asignacion de su valor

    if llave in Diccionario:                                                #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
            si = input('La clave es existente en el diccionario\nQuieres agregar un dato a ese diccionario?\n')       #pide un dato al usuario y lo guarda en una variable
            if (si == 'Si')or (si== 'si'):                                  #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
                dato  = input('Dame el dato que quieres agregar a la clave\n')    #pide un dato al usuario y lo guarda en una variable
                DatoAnterior = Diccionario[llave] +',' +dato             #Recupera el dato en el diccionario y agrega el nuevo dato a ese, usando la llave para acceder
                Diccionarioaux = {llave:DatoAnterior}                    #Agrega una llave y valor al Diccionarioaux
                Diccionario.update(Diccionarioaux)                       #Inserta una llave y valor en el diccionario
                Diccionarioaux.clear()                                   #Elimina todos los elementos del diccionario
                print('Los valores del diccionario son:\n',Diccionario)  #Imprime los valores del diccionario
            else:                                                        #Instruccion else donde si en el if correspondiente la condicion no se cumple, entra a este ciclo
                print('Adios')                                           #Imprime adios en el terminal
                quit()                                                   #Instruccion para salir del programa
    else:                                                                #Instruccion else donde si en el if correspondiente la condicion no se cumple, entra a este ciclo
            dato  = input('Dame el dato que quieres concatenar a la clave\n') #pide un dato al usuario y lo guarda en una variable
            Diccionarioaux = {llave:dato}                                 #Agrega una llave y valor al Diccionarioaux
            Diccionario.update(Diccionarioaux)                            #Inserta una llave y valor en el diccionario
            Diccionarioaux.clear()                                        #Elimina todos los elementos del diccionario
            print('Los valores del diccionario son:',Diccionario)         #Imprime los valores del diccionario
    salir = input('Desea agregar mas datos?\n')                           #Imprime un mensaje para el usuario
    if (salir=='no') or (salir=='No'):                       #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
        quit()