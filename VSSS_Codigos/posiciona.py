
import math
import FIRALib



def posicionaBAIXA(id,team,x,y):
    contador = 1
    while contador==1:
        
        if( team == True):
            PosicaoCarro = FIRALib.amareloCar(id)
        if( team == False):
            PosicaoCarro = FIRALib.AzulCar(id)

        
        if (y) > (PosicaoCarro[1]+0.61):## Se a bola estiver a direita do carrinho
            C = ((x) - (-PosicaoCarro[0]+0.72))
            B = ((y) - (PosicaoCarro[1]+0.61))
            if (x) < (-PosicaoCarro[0]+0.72):
                theta =  -(3.1 + math.atan(B/C))
                
            else:
                theta =  -math.atan(B/C)

        if (y) < (PosicaoCarro[1]+0.61):## Se a bola estiver a direita do Esquerda
            C = (-(x) + (-PosicaoCarro[0]+0.72))
            B = ((y) - (PosicaoCarro[1]+0.61))
            if (x) < (-PosicaoCarro[0]+0.72):
                theta =  ( math.atan(B/C) + 3.1)
            else:
                theta =  math.atan(B/C)
##################################################################################################################################################################

        print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   

        if( PosicaoCarro[2] + 1.55 > theta and PosicaoCarro[2] - 1.55 < theta ):
            if ((PosicaoCarro[2]+0.299) > theta):
        
                FIRALib.movimente(0,team,-20,-50)#direita


            if ((PosicaoCarro[2]- 0.299) < theta):

                FIRALib.movimente(0,team,-50,-20)#esquerda

            if((PosicaoCarro[2]+0.398) > theta and theta > (PosicaoCarro[2]- 0.398) ):

                FIRALib.movimente(0,team,-30,-30)
        else:
            if(theta < -2 and PosicaoCarro[2] > 2):
                FIRALib.movimente(0,team,-50,-20)#esquerda
            elif(theta > 2 and PosicaoCarro[2] < -2):
                FIRALib.movimente(0,team,-20,-50)#direita

            else:
                if( theta > 0):
                    if ((PosicaoCarro[2]+0.299 + 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((PosicaoCarro[2]- 0.299 + 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((PosicaoCarro[2]+0.298 +3) > theta and theta > (PosicaoCarro[2]- 0.298 + 3) ):

                        FIRALib.movimente(0,team,30,30)

                if( theta < 0):
                    if ((PosicaoCarro[2]+0.299 - 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((PosicaoCarro[2]- 0.299 - 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((PosicaoCarro[2]+0.298 -3) > theta and theta > (PosicaoCarro[2]- 0.298 - 3) ):

                        FIRALib.movimente(0,team,30,30)
        if (-PosicaoCarro[0]+0.72 + 0.05 > x and -PosicaoCarro[0]+0.72 - 0.05 < x) and (PosicaoCarro[1]+0.61 + 0.05 > y and PosicaoCarro[1]+0.61 - 0.05 < y):
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


        if (PosicaoBola[1]+0.61) > (PosicaoCarro[1]+0.61):## Se a bola estiver a direita do carrinho
            C = ((-PosicaoBola[0] + 0.72) - (-PosicaoCarro[0]+0.72))
            B = ((PosicaoBola[1]+  0.61) - (PosicaoCarro[1]+0.61))
            if (-PosicaoBola[0] + 0.72) < (-PosicaoCarro[0]+0.72):
                theta =  -(3.1 + math.atan(B/C))
            else:
                theta =  -math.atan(B/C)

        if (PosicaoBola[1]+0.61) < (PosicaoCarro[1]+0.61):## Se a bola estiver a direita do Esquerda
            C = (-(-PosicaoBola[0] + 0.72) + (-PosicaoCarro[0]+0.72))
            B = ((PosicaoBola[1]+  0.61) - (PosicaoCarro[1]+0.61))
            if (-PosicaoBola[0] + 0.72) < (-PosicaoCarro[0]+0.72):
                theta =  ( math.atan(B/C) + 3.1)
            else:
                theta =  math.atan(B/C)

###########################################################################################################
        print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   

        if( PosicaoCarro[2] + 1.55 > theta and PosicaoCarro[2] - 1.55 < theta ):
            if ((PosicaoCarro[2]+0.299) > theta):
        
                FIRALib.movimente(0,team,-20,-50)#direita


            if ((PosicaoCarro[2]- 0.299) < theta):

                FIRALib.movimente(0,team,-50,-20)#esquerda

            if((PosicaoCarro[2]+0.398) > theta and theta > (PosicaoCarro[2]- 0.398) ):

                FIRALib.movimente(0,team,-30,-30)
        else:
            if(theta < -2 and PosicaoCarro[2] > 2):
                FIRALib.movimente(0,team,-50,-20)#esquerda
            elif(theta > 2 and PosicaoCarro[2] < -2):
                FIRALib.movimente(0,team,-20,-50)#direita

            else:
                if( theta > 0):
                    if ((PosicaoCarro[2]+0.299 + 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((PosicaoCarro[2]- 0.299 + 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((PosicaoCarro[2]+0.298 +3) > theta and theta > (PosicaoCarro[2]- 0.298 + 3) ):

                        FIRALib.movimente(0,team,30,30)

                if( theta < 0):
                    if ((PosicaoCarro[2]+0.299 - 3) < theta):
        
                        FIRALib.movimente(0,team,20,50)#Esquerda


                    if ((PosicaoCarro[2]- 0.299 - 3) > theta):

                        FIRALib.movimente(0,team,50,20)#Direita
                
                    if((PosicaoCarro[2]+0.298 -3) > theta and theta > (PosicaoCarro[2]- 0.298 - 3) ):

                        FIRALib.movimente(0,team,30,30)
