from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

nav = webdriver.Chrome()
nav.get("https://ferendum.com/pt/")
nav.maximize_window()
t.sleep(3)
nav.find_element(By.NAME,"titulo").send_keys("A automação vai mudar sua vida? ")
nav.find_element(By.NAME,"descripcion").send_keys("Os bots estão cada vez mais frequentes em nossas vidas..")
nav.find_element(By.NAME,"creador").send_keys("Curso RPA com Python")
nav.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys("Digitar Email")
nav.find_element(By.ID,"op1").send_keys("Sim! Ela me ajuda muito..")
nav.find_element(By.ID,"op2").send_keys("Não! Estou com medo de perder o emprego..")
nav.find_element(By.NAME,"config_anonimo").click()
nav.find_element(By.NAME,"config_priv_pub").click()
nav.find_element(By.NAME,"config_un_solo_voto").click()
nav.find_element(By.NAME,"accept_terms_checkbox").click()
t.sleep(1)
nav.find_element(By.CSS_SELECTOR,'input[value="Criar enquete"]').click()
t.sleep(3)
nav.find_element_by_id("crear_votacion").click()
t.sleep(3)
texto = nav.find_element_by_id("textoACopiar").text
print(texto)
navegador.quit()
