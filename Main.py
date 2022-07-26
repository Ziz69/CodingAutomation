import pyautogui as pg
import time
import os

projeto = pg.prompt("Insira o nome do projeto:", title="Automação Coding")

# Definindo Pasta projeto
diretorio = projeto
localizacao = "C:\Programas em Python"
caminho = os.path.join(localizacao, diretorio)
pg.PAUSE = 0.7

# Criando pasta do projeto


def pasta_projeto():
    os.mkdir(caminho)

# Abrindo VS Code


def abrir_code():
    pg.alert("O programa vai rodar agora, não mova o mouse ou use o teclado.",
             title='Automação Coding')
    pg.hotkey("win")
    pg.write('VsCode')
    pg.press('enter')
    time.sleep(4)
    pg.hotkey('ctrl', 'k')
    pg.hotkey('ctrl', 'o')
    pg.write(caminho)
    pg.press('enter')

# Abrindo múica pra codar


def abrir_música():
    pg.hotkey('win')
    pg.write('chrome')
    pg.press('enter')
    pg.hotkey('ctrl', 't')
    pg.write('https://www.youtube.com/watch?v=f02mOEt11OQ')
    pg.press('enter')
