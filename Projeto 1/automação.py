import pyautogui
import time
import pandas as pd
import pyperclip

pyautogui.PAUSE = 1

# Acessar o site da empresa

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

# Fazer o login no sistema
pyautogui.click(x=973, y=426)
pyautogui.write("meu_login")

pyautogui.click(x=935, y=521)
pyautogui.write("minha_senha")

pyautogui.click(x=971, y=601)

time.sleep(5)

# Baixar os arquivos
pyautogui.click(x=510, y=330) 
pyautogui.click(x=1661, y=198) 
pyautogui.click(x=1485, y=623) 
time.sleep(5)

# Calcular os indicadores

tabela = pd.read_csv(r"D:\Usuario\Desktop\Projetos\Projeto 1", sep=";") 
print(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()

preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

# Passo 5: Enviar o e-mail

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=135, y=240)

pyautogui.write("gigiosantista1912@gmail.com")
pyautogui.press("tab")

pyautogui.press("tab")
pyperclip.copy("Relatorio de Compras")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")
texto = f"""
Prezados,

Segue o relatório de compras

Total Gasto: R${total_gasto:.2f}
Quantidade de Produtos: R${quantidade:.2f}
Preco Médio: R${preco_medio:.2f}

Qualquer coisa é só falar

Att
Giovanni.
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("enter")