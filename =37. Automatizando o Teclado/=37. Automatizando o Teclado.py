import pyautogui
import time

# Simular o atalho Windows + S
# pyautogui.hotkey('win', 's')
# time.sleep(1)
# pyautogui.write('calculadora')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'shift', 's')

time.sleep(1)
with pyautogui.hold('winleft'):
    pyautogui.press('left')

time.sleep(2)
pyautogui.click()
time.sleep(2)
with pyautogui.hold('winleft'):
    pyautogui.press('right')