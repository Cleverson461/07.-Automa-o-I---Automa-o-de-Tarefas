import pyautogui
from time import sleep

with open('files/alunos.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # print(line.split(',')[0])
        # print(line.split(',')[1])
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        
        pyautogui.click(402, 399, duration=1)
        sleep(1)
        pyautogui.write(aluno)
        pyautogui.click(398, 433, duration=1)
        pyautogui.write(email)
        sleep(1)
        pyautogui.click(412, 454, duration=1)
        pyautogui.screenshot(f'files/{aluno}.png')
        sleep(1)
        
        