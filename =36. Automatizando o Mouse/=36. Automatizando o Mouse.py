import pyautogui
import time

# 1 - Tamanho da tela
print(pyautogui.size())

# 2 - Pegar a Posição Atual do Cursor
print(pyautogui.position())
time.sleep(1.5)

# 3 - App para vê a posição do mouse em tempo real
# python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Mover o cursor do Mouse
pyautogui.moveTo(1325, 16, 1)
time.sleep(1.5)
pyautogui.click()

# 5 - Realizando o Scrool
time.sleep(1.5)
pyautogui.moveTo(632, 638)
pyautogui.click()
time.sleep(1.5)
pyautogui.scroll(-900)