import FIRALib
import posiciona

## modelando o coleirão
##Goleiro Amarelo


##colocar o carrinho na posição certa
posicionador = 0
orientador = 0
while True:

    Bola = FIRALib.bola()
    Tafareu = FIRALib.amareloCar(0)
    FIRALib.movimente(1,False,50,-1000)
##girar o rainho na orientação -1.5
    
    if posicionador == 0:
        posiciona.posicionaBAIXA(0,True,0.02,0.6)


        posicionador = 1
        
        print("CHEGEUI!!")
        
    if orientador == 0:
        FIRALib.movimente(0,True,-1,1)
        print(Tafareu[2])

        if Tafareu[2] > -1.52 and Tafareu[2] < -1.50:
            FIRALib.movimente(0,True,0,0)
            orientador = 1

        if Tafareu[2] < 1.52 and Tafareu[2] > 1.50:
            FIRALib.movimente(0,True,0,0)
            orientador = 1
    
    if orientador == 1:
        print(Tafareu[1])
        if Tafareu[1]> Bola[1]:
            FIRALib.movimente(0,True,25,25)
        if Tafareu[1]< Bola[1]:
            FIRALib.movimente(0,True,-25,-25)
        if (Tafareu[1]+0.61)< 0.36:
            FIRALib.movimente(0,True,-30,-30)
        if Tafareu[1]+0.61> 0.78:
            FIRALib.movimente(0,True,30,30)




        
        



##seguir a bola 










##Goleiro Azul