import pyautogui
import time

pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('edge')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(247, 90)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.write('youtube Eddie Pinero')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(247, 744)
time.sleep(1)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(522, 477)
time.sleep(3)
pyautogui.press('enter')
time.sleep(1)
pyautogui.alert(title='Agradecimento', text='Obrigado por se increver no canal', button='OK')