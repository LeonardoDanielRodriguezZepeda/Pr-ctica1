ConjuntoNumerosReales=set([0,1,2,3,4,5,6,7,8,9,10])                                 #Creacion del una tupla con numeros reales
ConjuntoVacio= set()                                                                #Creacion de tupla vacia
ConjuntoPractica = set()                                                            #Creacion de tupla vacia
b=0                                                                                 #Declaracion de variable b=0

def Funcion_Operacion(a=None,A=None):                                               #Declaracion de funcion Funcion_Operacion con dos argumentos

  if a=="1":                                                                        #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
     ConjuntoC = ConjuntoNumerosReales|ConjuntoPractica                             #Operacion union de el ConjuntoNumerosReales y ConjuntoPractica
     ConjuntoD = ConjuntoVacio | ConjuntoPractica                                    #Operacion union de el ConjuntoVacio y ConjuntoPractica
     for n in ConjuntoC:                                                            #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoC
         str(n)                                                                     #Convierte n a string
         print("La union de los numeros reales y tu conjunto es igual a:",n)        #Imprime un mensaje al usuario
     for n in ConjuntoD:                                                            #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoD
         str(n)                                                                    #Convierte n a string
         print("La union del conjunto vacio y tu conjunto  es igual a:",n)         #Imprime un mensaje al usuario
       
  if a=="2":                                                                        #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
        ConjuntoC = ConjuntoNumerosReales & ConjuntoPractica                        #Operacion interseccion de el ConjuntoNumerosReales y ConjuntoPractica
        ConjuntoD = ConjuntoVacio & ConjuntoPractica                                #Operacion interseccion de el ConjuntoNumerosReales y ConjuntoPractica
        for n in ConjuntoC:                                                         #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoC
         str(n)                                                                     #Convierte n a string
         print("La interseccion de los numeros reales y tu conjunto es igual a:",n) #Imprime un mensaje al usuario
        for n in ConjuntoD:                                                        #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoD
         str(n)                                                                     #Convierte n a string
         print("La interseccion del conjunto vacio y tu conjunto  es igual a:",n)   #Imprime un mensaje al usuario 
  if a=="3":                                                                        #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
       ConjuntoC = ConjuntoNumerosReales-ConjuntoPractica                           #Operacion diferencia de el ConjuntoNumerosReales y ConjuntoPractica
       ConjuntoD = ConjuntoVacio - ConjuntoPractica                                 #Operacion diferencia de el ConjuntoNumerosReales y ConjuntoPractica
       for n in ConjuntoC:                                                          #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoC
         str(n)                                                                     #Convierte n a string
         print("La diferencia de los numeros reales y tu conjunto es igual a:",n)   #Imprime un mensaje al usuario
       for n in ConjuntoD:                                                          #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoD
         str(n)                                                                     #Convierte n a string
         print("La diferencia del conjunto vacio y tu conjunto  es igual a:",n)    #Imprime un mensaje al usuario
  if a=="4":                                                                       #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
      ConjuntoC = ConjuntoNumerosReales^ConjuntoPractica                           #Operacion diferencia simetrica de el ConjuntoNumerosReales y ConjuntoPractica
      ConjuntoD = ConjuntoVacio ^ ConjuntoPractica                                 #Operacion diferencia simetrica de el ConjuntoNumerosReales y ConjuntoPractica
      for n in ConjuntoC:                                                           #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoC
         str(n)                                                                     #Convierte n a string
         print("La diferencia simetrica de los numeros reales y tu conjunto es igual a:",n)  #Imprime un mensaje al usuario
      for n in ConjuntoD:                                                                    #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable ConjuntoD
         str(n)                                                                              #Convierte n a string
         print("La diferencia simetrica del conjunto vacio y tu conjunto  es igual a:",n)    #Imprime un mensaje al usuario
  if a=="5":                                                                                 #Instruccion condicional donde si la condicion se cumple, entra a realizar el codigo dentro del if
      quit()                                                                        #Instruccion para salir del programa                              
def inicio_calculos():                                                              #Declaracion de la funcion inicio_calculos
    while b<6:                                                                                                           #Sentencia while usada en este caso como un bucle infinito
        print("Selecciona una operación:\n1-Unión\n2-Intersección\n3-Diferencia\n4-Diferencia simétrica\n5-salir")       #Imprime el mensaje asignado para el usuario
        seleccion = input()                                                              #Guarda el dato que el usuario introdujo en una variable
        valores =input("De que tamaño quieres tu conjunto A")                            #Pide un valor al usuario y lo guarda en una variable
        x=range(int(valores))                                                            #Conversion de la variable valores a entero y se declara el tipo range para la secuencia de numeros
        for n in  x:                                                                     #Ciclo for funciona para hacer iteraciones dependiendo del valor de la variable x
            c  =   input("Dame el valor del temino del conjunto A en la posición:")      #Pide un valor al usuario y lo asigna a una variable
            ConjuntoPractica.add(c)                                                      #Agrega los valores introducidos por el usuario a la tupla ConjuntoPractica
        Funcion_Operacion(seleccion,ConjuntoPractica)                                    #Llamada a la funcion Funcion_Operacion con dos argumentos                           


if _name_ == '_main_':                                                                  #main
      inicio_calculos()                                                                 #Llamada a la funcion inicio_calculos sin argumentos