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
pyautogui.write('ibovespa hoje')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.screenshot('ibovespa.png')