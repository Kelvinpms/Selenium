from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

navegador = webdriver.Chrome()
navegador.get("https://consultacnpj.com/cnpj/")
navegador.maximize_window()
t.sleep(2)
cnpjs = ["45997418000153", "72273196001090", "33000167000101"]

for cnpj in cnpjs:
    input = navegador.find_element(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input')
    input.clear()
    input.send_keys(cnpj)
    t.sleep(1)
    texto = navegador.find_element(By.XPATH,'//*[@id="company-data"]')
    with open(f'{str(cnpj)}.csv', 'w', encoding="UTF-8") as csv:
            csv.write(texto.text)
    t.sleep(2)

navegador.quit()