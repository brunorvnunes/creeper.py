import os
import time
import pyautogui as py 
import time as tm 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.firefox.service import service 



browser = webdriver.Firefox()
velocidade = 0.3
py.moveTo(500, 70)
tm.sleep(0.5)
py.click(button='left')
py.write('https://gmail.google.com' interval=0.1)
py.press('enter')
tm.sleep(10)
py.moveTo(924, 322)
py.click(button='left')
py.write('bruno_r_nunes@estudante.sesisenai.org.br' interval=0.1)
py.press('enter')
tm.sleep(10)
py.write('Bruno321')
tm.sleep(10)
py.press('enter')
tm.sleep(10)
py.moveTo(557, 61)
py.click(button= 'left')
py.write('https://docs.google.com/forms/d/e/1FAIpQLScr_0O_qwNQDGxW8mQNhZhM-V6F9TwJFGjCEB6Xykh1ncRUeg/viewform' interval=0.1)
tm.sleep(1)
py.press('enter')
tm.sleep(1)
py.alert('Iniciando processo')
py.moveTo(397, 664)
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(1361, 382) #barrinha pra mover
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(456, 202) #mover escolher
tm.sleep(1)
py.click(button= 'left') #selecionar
tm.sleep(1)
py.moveTo(454, 228)#mover
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(415, 385)#mover Quantidade produzida no lote
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.write('40')
tm.sleep(1)
py.press('enter')
tm.sleep(1)
py.moveTo(398, 515) # Meta alcançada
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(412, 633) #avançar
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
#PROXIMO PASSO!!!

py.moveTo(1364, 411) #barrinha pra mover
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(434, 133)#mover escolher
tm.sleep(1)
py.click(button='left')#selecionar
tm.sleep(1)
py.moveTo(421, 259)#mover
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(447, 293 )#mover Quantidade produzida no lote
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.write('39')
tm.sleep(1)
py.moveTo(396, 465)# Meta alcançada
tm.sleep(1)
py.click(button='left')
tm.sleep(1)
py.moveTo(521, 577)#avançar
tm.sleep(1)
py.click(button='left')
tm.sleep(1)

# TERCEIRO PASSO !!

py.moveTo(1364, 411) #barrinha pra mover
tm.sleep(1)
py.click(button='left')
py.moveTo(434, 133)#mover escolher
tm.sleep(1)
py.click(button='left')#selecionar