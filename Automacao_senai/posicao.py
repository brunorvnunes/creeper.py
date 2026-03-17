import pyautogui as py
import time as tm 

py.alert('Calma!')
tm.sleep(6)
posicao = py.position()
tm.sleep(1)
print(posicao)

