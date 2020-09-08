import time
from random import randint

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InstagramBot:
    def __init__(self, listaPerfis, caminho):
        self.listaPerfis = listaPerfis
        self.caminho = caminho
        self.driver = webdriver.Firefox(executable_path = self.caminho)
        self.logado = False
        self.trocar = False
        self.perfil = 0
        self.contador = 0
        self.abas = list()
        self.perfis = list()

    def pegarUrl(self): #segunda aba (pegar url)
        driver = self.driver
        time.sleep(randint(2, 5))
        #Se for uma publicação:
        if '/p' in driver.current_url:
            time.sleep(randint(2, 5))
            tag = driver.find_elements_by_tag_name('a')
            hrefs = [elem.get_attribute('href') for elem in tag]

            url = hrefs[0]
        else:    
            time.sleep(randint(2, 5))
            #Pegando a url do instagram:
            url = driver.current_url
        nova = url[26:(len(url)-1)]
        return nova

    def logarInsta(self):
        driver = self.driver
        url = self.pegarUrl() #pegar url
        driver.get("https://www.instagram.com/") #terceira aba (login no instagram)
        time.sleep(randint(2, 5))

        #trocar perfil
        if self.trocar:
            classe = driver.find_element_by_class_name('HoLwm')
            classe.click()
            time.sleep(randint(2, 5))
            classe = driver.find_element_by_class_name('gmFkV')
            classe.click()
            time.sleep(randint(2, 5))
            sair = driver.find_element_by_class_name('wpO6b')
            sair.click()
            time.sleep(randint(2, 5))
            sair = driver.find_element_by_xpath('//button[text()="Sair"]')
            sair.click()

            self.logado = False
            self.trocar = False

        time.sleep(randint(2, 5))

        if self.logado == False:
            #Input de dados
            while True:
                try:
                    campo_username = driver.find_element_by_xpath("//input[@name='username']")
                    campo_username.click()
                    time.sleep(randint(2, 5))
                    campo_username.send_keys(self.listaPerfis[self.contador])

                    campo_password = driver.find_element_by_xpath("//input[@name='password']")
                    campo_password.click()
                    time.sleep(randint(2, 5))
                    campo_password.send_keys(self.listaPerfis[self.contador+1])
                    
                    time.sleep(randint(2, 5))
                    campo_password.send_keys(Keys.RETURN)
                    break
                except:
                    self.logarInsta()
            
            #Não salvar:
            time.sleep(randint(2, 5))  
            salvar = driver.find_element_by_xpath("//button[text()='Agora não']")
            salvar.click()
            
            #Ativar notificações:
            time.sleep(randint(2, 5))
            classe = driver.find_element_by_class_name('HoLwm')   
            classe.click()
            self.logado = True  
            self.contador += 2

        #Pesquisar
        try:
            time.sleep(randint(2, 5))
            buscar = driver.find_element_by_class_name('TqC_a')
            buscar.click()
            time.sleep(randint(2, 5))
            buscar = driver.find_element_by_xpath('//input[@data-focus-visible-added=""]')
            buscar.click()
            time.sleep(randint(2, 5))
            buscar.clear()
            time.sleep(randint(2, 5))
            buscar.send_keys(url)
            time.sleep(randint(1, 5))
            buscar = driver.find_element_by_xpath('//a[@href="/' + url + '/"]')
            buscar.click()
            time.sleep(randint(1, 5))
        except:
            self.logarInsta()
            time.sleep(5)

        if driver.current_url != ('https://www.instagram.com/' + url + '/'): #se a url de pesquisa for igual a url referência:
            driver.get('https://www.instagram.com/' + url + '/')
        #Clicando em seguir:
        try:
            seguir = driver.find_element_by_class_name('_6VtSN')
            seguir.click()
            time.sleep(randint(1, 5))
        except:
            return False

        try:
            classe = driver.find_element_by_class_name('HoLwm')
            classe.click()
            time.sleep(randint(1, 5))
            driver.refresh()
        except:
            return False

        try:
            xpath = driver.find_element_by_xpath('//button[text()="OK"]')
            xpath.click()
            time.sleep(5)
            driver.refresh()
        except:
            return False   

    def loginInstelike(self):
        driver = self.driver
        #Primeira aba (login no instelikes)
        driver.get("https://instelikes.com.br/app?share=REF-hukeAAAAAAA#login")
        self.abas.append(driver.window_handles[0])
        driver.switch_to_window(self.abas[0])

        #Input de dados:
        try:
            time.sleep(3)
            campo_email = driver.find_element_by_xpath('//input[@name="email"]')
            campo_email.click()
            campo_email.send_keys(self.listaPerfis[self.contador])
            campo_email.send_keys(Keys.RETURN)
            time.sleep(3)
            campo_senha = driver.find_element_by_xpath('//input[@name="password"]')
            campo_senha.click()
            campo_senha.send_keys(self.listaPerfis[self.contador+1])
            campo_senha.send_keys(Keys.RETURN)
        except:
            driver.refresh()
            time.sleep(3)
            self.abas.clear()
            self.contador=0
            self.loginInstelike()

        #Selecionar perfil:
        time.sleep(3)
        usuario = driver.find_element_by_xpath("/html/body/main/x-active-template/div/div/div/div/div/div/form/x-active-template/div[1]/div[1]/div")
        usuario.click()

        #Verificar o número de perfis:
        time.sleep(3)
        cont = 1
        path = self.checarBotao('/html/body/aside[1]/div[2]/ul[2]/li[4]/div/div/div/div[2]/a['+str(cont)+']/div')
        while path:
            self.perfis.append('/html/body/aside[1]/div[2]/ul[2]/li[4]/div/div/div/div[2]/a['+str(cont)+']/div')     
            cont += 1 
            path = self.checarBotao('/html/body/aside[1]/div[2]/ul[2]/li[4]/div/div/div/div[2]/a['+str(cont)+']/div')     
        
        print(f'Número de perfis: {len(self.perfis)}')
        
        #Botão ganhe moedas: 
        earn_coins = driver.find_element_by_xpath('//a[@data-text="earn-coins"]')
        earn_coins.click()

    def entrarDireto(self):
        driver = self.driver
        try:
            driver.find_element_by_class_name('_6VtSN').click()
            time.sleep(randint(1, 5))
        except:
            return False
        return True

        try:
            driver.find_element_by_class_name('HoLwm').click()
            time.sleep(randint(1, 5))
        except:
            return False
        return True    

        try:
            driver.find_element_by_xpath('//button[text()="OK"]').click()
            time.sleep(randint(1, 5))
            driver.refresh()
        except:
            return False        
        return True    

    def trocarPerfil(self):
        driver = self.driver
        if len(self.abas) >= 1:    
            driver.switch_to_window(self.abas[0])
        print('abas: ',self.abas)
        time.sleep(1)
        try:
            confirmar = driver.find_element_by_xpath('//button[@data-text="confirm"]')
            confirmar.click()    
            time.sleep(1)
        except:
            time.sleep(1)

        if len(self.abas) >= 1:    
            self.abas.pop()   
        time.sleep(2)    
        print('abas: ',self.abas)  

        try:       
            time.sleep(1)
            buscar = driver.find_element_by_xpath('/html/body/aside[1]/div[2]/ul[2]/li[4]/div/img')
            buscar.click()
            time.sleep(1)
            if self.perfil >= (len(self.perfis)-1):
                self.perfil = 0
            else:
                self.perfil += 1
            buscar = driver.find_element_by_xpath(self.perfis[self.perfil])
            buscar.click()
            time.sleep(1)
            self.trocar = True
        except:
            self.trocarPerfil()
            time.sleep(5)            

    def selecionarPerfil(self):
        driver = self.driver
        if self.logado:
            #Voltar a página anterior:
            if len(self.abas) > 1:    
                driver.switch_to_window(self.abas[0])                
            try:
                buscar = driver.find_element_by_xpath('//button[@data-text="confirm"]')
                buscar.click()
                time.sleep(2)
            except:
                time.sleep(2)

            if len(self.abas) > 1:    
                self.abas.pop()                
            time.sleep(5) 

            if (self.checarBotao('/html/body/main/x-active-template/div/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/form') == False) or (self.trocar == True):
                try:
                    time.sleep(1)
                    select = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/form/div/div/div[1]')
                    select.click()
                    time.sleep(1)
                    select = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/form/div/div/div[3]/div/label[2]/input')
                    select.click()
                    time.sleep(1)
                    select = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/form/button')
                    select.click()
                    time.sleep(1)
                    #Botão Ganhe moedas
                    earn_coins = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/form')
                    earn_coins.click()
                except:
                    self.selecionarPerfil()
                    time.sleep(5)
            else:
                atualizar = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/form')
            time.sleep(3)
        
        else:
            try:
                time.sleep(1)
                select = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/form/div/div/div[1]')
                select.click()
                time.sleep(1)
                select = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/form/div/div/div[3]/div/label[2]/input')
                select.click()
                time.sleep(1)
                select = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/form/button')
                select.click()
                time.sleep(1)
                #Botão Ganhe moedas
                earn_coins = driver.find_element_by_xpath('/html/body/main/x-active-template/div/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/form')
                earn_coins.click()
            except:
                self.selecionarPerfil()
                time.sleep(5)

        while True:
            try:
                self.abas.append(driver.window_handles[1])
                driver.switch_to_window(self.abas[1])
                break
            except:
                self.selecionarPerfil()
                time.sleep(5)       

    def checarBotao(self, xpath):
        self.xpath = xpath
        driver = self.driver
        try:
            driver.find_element_by_xpath(self.xpath)
        except:
            return False    
        return True    

    def getSessao(self):
        if self.logado:
            return True
        else:
            return False     
