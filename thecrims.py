from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,urlretrieve
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui,time
#Acessando a pagina
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.thecrims.com/#/')

#Variaveis de acesso:
name = input('Name:')
pw = input('Passaword:')

#Entrando na conta
try:
    def up_Sit():
        pyautogui.click(770,269)
        pyautogui.typewrite(name)
        pyautogui.click(776,316)
        pyautogui.typewrite(pw)
        pyautogui.click(743,368)        
except:
    ('Coloque apenas letras')
  
#Passando isntrucao de funcoes escolhendo as funcoes
roubo = (382,792)
puteiro_1 = (475,543)
puta =(741,537)
sair_puteiro = (731,426)
contagem_roubos = 0
tiket_puteiro = 235
def roubar():
    global contagem_roubos
    driver.find_element_by_id('menu-robbery').click()
    time.sleep(2)
    driver.find_element_by_id('singlerobbery-select-robbery').click()
    time.sleep(2)
    pyautogui.moveTo(roubo,duration=0.25)
    time.sleep(2)
    pyautogui.scroll(-200)
    time.sleep(2)
    pyautogui.click(roubo)
    for i in range(2):
        time.sleep(0.75)
        contagem_roubos+=1
        driver.find_element_by_id('singlerobbery-rob').click()

def puteiro():
    global tiket_puteiro
    driver.find_element_by_id('menu-nightlife').click()
    time.sleep(2)
    pyautogui.click(puteiro_1)
    time.sleep(1)
    pyautogui.click(puta)
    time.sleep(1)
    pyautogui.click(sair_puteiro)
    tiket_puteiro = tiket_puteiro - 1
    
#Criando coteiro temporal
up_Sit()
for i in range(250):
    time.sleep(2)
    roubar()
    print(f"Numero de roubos:{contagem_roubos}")
    time.sleep(2)
    puteiro()
    print(f"Numero de tiketes{tiket_puteiro}")
tiket_perdidos = 235 - tiket_puteiro
print(f'Numero de tiketes perdidos:{tiket_perdidos}')
time.sleep(3)
driver.quit()





