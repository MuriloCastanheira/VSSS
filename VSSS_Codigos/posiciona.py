
import math
import FIRALib



def posicionaBAIXA(id,team,x,y):
    contador = 1
    
    while contador==1:
        
        if( team == True):
            PosicaoCarro = FIRALib.amareloCar(id)
        if( team == False):
            PosicaoCarro = FIRALib.AzulCar(id)

        
        pc1 = PosicaoCarro[1] + 0.61
        pc2 =-PosicaoCarro[0] + 0.72
        pc3 = PosicaoCarro[2] + 1.55
        pc4 = PosicaoCarro[2] - 1.55
        pc5 = PosicaoCarro[2] + 0.299
        pc6 = PosicaoCarro[2] - 0.299
        pc7 = PosicaoCarro[2] + 0.298
        pc8 = PosicaoCarro[2] - 0.298
        pc9 = PosicaoCarro[2] + 0.398
        pc10 = PosicaoCarro[2] - 0.398
        if (y) > (pc1):## Se a bola estiver a direita do carrinho
            C = ((x) - (pc2))
            B = ((y) - (pc1))
            if (x) < (pc2):
                theta =  -(3.1 + math.atan(B/C))
                
            else:
                theta =  -math.atan(B/C)

        if (y) < (pc1):## Se a bola estiver a direita do Esquerda
            C = (-(x) + (pc2))
            B = ((y) - (pc1))
            if (x) < (pc2):
                theta =  ( math.atan(B/C) + 3.1)
            else:
                theta =  math.atan(B/C)
##################################################################################################################################################################

        #print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   

        if( pc3 > theta and pc4 < theta ):
            if ((pc5) > theta):
        
                FIRALib.movimente(0,team,-20,-50)#direita


            if ((pc6) < theta):

                FIRALib.movimente(0,team,-50,-20)#esquerda

            if((pc9) > theta and theta > (pc10) ):

                FIRALib.movimente(0,team,-30,-30)
        else:
            if(theta < -2 and PosicaoCarro[2] > 2):
                FIRALib.movimente(0,team,-50,-20)#esquerda
            elif(theta > 2 and PosicaoCarro[2] < -2):
                FIRALib.movimente(0,team,-20,-50)#direita

            else:
                if( theta > 0):
                    if ((pc5 + 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((pc6 + 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((pc7 +3) > theta and theta > (pc8 + 3) ):

                        FIRALib.movimente(0,team,30,30)

                if( theta < 0):
                    if ((pc5 - 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((pc6 - 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((pc7 -3) > theta and theta > (pc8 - 3) ):

                        FIRALib.movimente(0,team,30,30)
        if (pc2+ 0.05 > x and pc2 - 0.05 < x) and ( pc1 + 0.05 > y and pc1 - 0.05 < y):
            FIRALib.movimente(id,team,0,0) 
            contador = 0




def SeguiBola(id,team):

    while True:
        PosicaoBola = FIRALib.bola()
    ## FIRALib.movimente(0,True,1,-1)
        if( team == True):
            PosicaoCarro = FIRALib.amareloCar(id)
        if( team == False):
            PosicaoCarro = FIRALib.AzulCar(id)

        pc1 = PosicaoCarro[1] + 0.61
        pc2 =-PosicaoCarro[0] + 0.72
        pc3 = PosicaoCarro[2] + 1.55
        pc4 = PosicaoCarro[2] - 1.55
        pc5 = PosicaoCarro[2] + 0.299
        pc6 = PosicaoCarro[2] - 0.299
        pc7 = PosicaoCarro[2] + 0.298
        pc8 = PosicaoCarro[2] - 0.298
        pc9 = PosicaoCarro[2] + 0.398
        pc10 = PosicaoCarro[2] - 0.398
        pb1 = PosicaoBola[1] + 0.61
        pb2 = -PosicaoBola[0] + 0.72

        if (pb1) > (pc1):## Se a bola estiver a direita do carrinho
            C = ((pb2) - (pc2))
            B = ((pb1) - (pc1))
            if (pb2) < (pc2):
                theta =  -(3.1 + math.atan(B/C))
            else:
                theta =  -math.atan(B/C)

        if (pb1) < (pc1):## Se a bola estiver a direita do Esquerda
            C = (-(pb2) + (pc2))
            B = ((pb1) - (pc1))
            if (pb2) < (pc2):
                theta =  ( math.atan(B/C) + 3.1)
            else:
                theta =  math.atan(B/C)

###########################################################################################################
       # print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   

        if( pc3 > theta and pc4 < theta ):
            if ((pc5) > theta):
        
                FIRALib.movimente(0,team,-20,-50)#direita


            if ((pc6) < theta):

                FIRALib.movimente(0,team,-50,-20)#esquerda

            if((pc9) > theta and theta > (pc10) ):

                FIRALib.movimente(0,team,-33,-33)
        else:
            if(theta < -2 and PosicaoCarro[2] > 2):
                FIRALib.movimente(0,team,-50,-20)#esquerda
            elif(theta > 2 and PosicaoCarro[2] < -2):
                FIRALib.movimente(0,team,-20,-50)#direita

            else:
                if( theta > 0):
                    if ((pc5 + 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((pc6+ 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((pc7 +3) > theta and theta > (pc8 + 3) ):

                        FIRALib.movimente(0,team,33,33)

                if( theta < 0):
                    if ((pc5 - 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((pc6- 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((pc7 -3) > theta and theta > (pc8- 3) ):

                        FIRALib.movimente(0,team,33,33)
