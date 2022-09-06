
class humano:                   #Declaracion de la clase

 brazos=2                         #Atributo de la clase
 cabeza=1                         #Atributo de la clase
 piernas=2                        #Atributo de la clase
 ojos=2                           #Atributo de la clase
 manos=2                          #Atributo de la clase
 dedos=20                         #Atributo de la clase
 def _init_(color,estatura,complexion):         #Constructor

    self.color = color                          #Atributo de instancia
    self.estatura = estatura                    #Atributo de instancia
    self.complexion = complexion                #Atributo de instancia
def raza(self):                          #Metodo
      if self.color == 'blanco':         #Sentencia condicional
        print('Caucasico')               #Imprime un mensaje 
      if self.color == 'negro':          #Sentencia Condicional
            print('Negro')               #Imprime un mensaje 
         
if __name__ == '__main__':                   #Main
    persona1 = humano()                      #Crea objeto de clase humano
    color1 = input('Dame el color de piel')  #Ponemos un valor a la variable de instancia
    estatura1 = input('Dame la estatura')    #Ponemos un valor a la variable de instancia
    complexion1 = input('Dame la complexion') #Ponemos un valor a la variable de instancia
    persona1._init_(color1,estatura1,complexion1) #Llamamos al contructor
    print('La persona tiene brazos =',persona1.brazos) #Imprime el numero de brazos, llamando al atributo

