import pyautogui
from time import sleep
Fulano
with open('files/alunos.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # print(line.split(',')[0])
        # print(line.split(',')[1])
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        
        pyautogui.click(505, 495, duration=1)
        sleep(1)
        pyautogui.write(aluno)
        pyautogui.click(493, 535, duration=1)
        pyautogui.write(email)
        sleep(1)
        pyautogui.click(516, 555, duration=1)
        pyautogui.screenshot(f'files/{aluno}.png')
        sleep(1)
        
        