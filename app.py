from selenium import webdriver
from selenium.webdriver.common.by import By  
from time import sleep 
import pyautogui

driver = webdriver.Chrome()
driver.get('https://site_exemplo.com')
sleep(5)


driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

botao_carregar_mais = driver.find_element(By.XPATH, "//button[@id='loadMoreBtn']")  
sleep(2)
botao_carregar_mais.click()
sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  
sleep(1)
driver.execute_script('window.scrollTo(0, 0);')
sleep(2)


botao_carregar_planilha_produtos = driver.find_element(By.XPATH, "//label[@for='fileInput']")
sleep(2)
botao_carregar_planilha_produtos.click()
sleep(5)
pyautogui.write(r'C:\Users\user\Downloads\precos-produtos-atualizados.xlsx')
sleep(2)
pyautogui.press('enter')
input('Aperte enter no terminal para fechar o programa')