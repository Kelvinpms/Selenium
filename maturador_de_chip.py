from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import urllib
import csv
import random

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID,"side")) < 1:
    sleep(1)

# já estamos com o login feito no whatsapp web
input_file = 'Mensagens.txt'
lista = ['8599404532','3189528362','3186474381','8597166322','2184961540']

with ThreadPoolExecutor() as executor:
    # Envie as tarefas para o pool de threads para serem processadas em paralelo
    with open(input_file, 'r') as data:
        reader = csv.reader(data, delimiter='\t')
        for row in reader:
            for number1 in lista:
                # Gera um novo valor de number1 a cada iteração do loop
                number1_list = list(number1)  # transforma a string em uma lista de caracteres
                #random.shuffle(number1_list)  # embaralha a lista de caracteres
                number1 = ''.join(number1_list)  # transforma a lista de caracteres em uma string
                
                # Gera um novo valor de row_string a cada iteração do loop
                row_string = ' '.join(row)
                row_string = row_string.replace(" ' ", "  ").replace(" [ ", "  ").replace(" ] ", "  ")
                
                executor.submit(row)
                row_string1= urllib.parse.quote(f"{row_string}")
                link = f"https://web.whatsapp.com/send?phone="+number1+"&text="+row_string1
                print(link)
                navegador.get(link)
                #while len(navegador.find_elements(By.CSS_SELECTOR, "//div[class='_3HQNh _1Ae7k']")) < 1:
                while len(navegador.find_elements(By.ID,"side")) < 1:
                    sleep(1)
                sleep(5)    
                clicar = navegador.find_element(By.XPATH, '//div[@class="_3HQNh _1Ae7k"]')
                sleep(5)
                clicar.click()
                sleep(10)
