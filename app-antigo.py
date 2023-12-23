from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #para trabalhar com elementos que talvez ainda nao existam no DOM
from selenium.webdriver.support import expected_conditions as EC #esperar pela presença de um elemento
import time

pagina = 'https://amberlive.000webhostapp.com/pagina.html'

driver = webdriver.Chrome()
driver.get(pagina)
# elem = driver.find_element(By.ID, "Login")
# elem.send_keys("0028")
# elem = driver.find_element(By.ID, "Password")
# elem.send_keys("Claudiane.1")
# elem.send_keys(Keys.RETURN)
# elem.find_element(By.XPATH, "//*[text()='Processos Internos']")
# elem.click()

# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
time.sleep(5)

#clico na opcao de devolucao
elem = driver.find_element(By.ID, "OriginalAddress_Devolution")
elem.click()
#clico no campo Produto
prod = driver.find_element(By.ID, "Product_Name")
prod.click()
#digito o codigo e aperto Enter
prod.send_keys()
#seleciono o botao do endereço de origem
#escolho o produto com base no lote
#verifico se a quantidade tá certa
#se nao tiver certa, escrevo a quantidade certa
#seleciono no botao para mostrar a posicao de devolucao
#clico na posicao da devolucao
#e clico no botao verde