from InstagramBot import *

listaPerfis = []
try:
    file = open('contas.txt', 'r')
    for i in file:
        if i != '\n':
            corte = i
            listaPerfis.append(corte[:-1])
finally:        
    file.close()   

caminho = ''
try:
    arquivo = open('caminho.txt', 'r')
    if '\n' in arquivo.read():
        arquivo.seek(0)
        caminho = arquivo.read()[:-1]
    else:    
        arquivo.seek(0)
        caminho = arquivo.read()
finally:        
    arquivo.close()
    if '\n' in caminho:    
        print(caminho)

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
