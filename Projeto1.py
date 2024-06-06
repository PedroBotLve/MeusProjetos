'''
 Projeto de automação, Jornada Python.
 Nome: Pedro Abade.
'''
#importando bibliotecas.
import pyautogui as py
import pandas as pd
import time
#Automatizando um processo de preenchimento de dados em um site.
#Acessando o navegador(Chrome).
py.PAUSE=1
py.press("win")
py.write("Chrome")
py.press("enter")
time.sleep(5)
py.click(x=555, y=322)
time.sleep(8)
#Acessando o site disponiilizado pelo Curso Jornada Python.
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
time.sleep(8)
#Realizando o loin(Login e senha aleatorio).
py.click(x=468, y=373)
py.write("Bongionro_Geovanna4@gmail.com")
py.press("tab")
py.write("filhodoDio123")
py.press("tab")
py.press("enter")
time.sleep(8)
#importando a tabela com os dados formatados.
tabela=pd.read_csv("C:\\Users\\Usuario\\Downloads\\python\\aula1\\produtos.csv")
#Preenchendo dados.
for linha in tabela.index:
    py.click(x=448, y=256)#Meu monitor.
    py.write(str(tabela.loc[linha, "codigo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "custo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter")
    py.scroll(5000)   
#enviar para o sistema e repetir o processo de preenchimento de dados.
