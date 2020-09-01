from InstagramBot import *

listaPerfis = []
try:
    file = open('contas.txt', 'r')
    for i in file:
        corte = i
        listaPerfis.append(corte[:-1])
finally:        
    file.close()    

caminho = ''
try:
    arquivo = open('caminho.txt', 'r')
    caminho = arquivo.readline()
    #caminho = caminho[:-1]
finally:        
    arquivo.close()

robo = InstagramBot(listaPerfis, caminho)        
cont = 0
robo.loginInstelike()#0
while True: 
    robo.selecionarPerfil()#1
    if (randint(1,10) > 7) and robo.getSessao():
        robo.entrarDireto()#2
    else:    
        robo.logarInsta()#2     

    if cont >= 0: 
        robo.trocarPerfil()   
        cont = 0    
    cont += 1   
