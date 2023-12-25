from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #para trabalhar com elementos que talvez ainda nao existam no DOM
from selenium.webdriver.support import expected_conditions as EC #esperar pela presença de um elemento
import time
from app2_openpyxl import Produtos



class Navegador():
    
    def __init__(self):
        self.linha = 0
        self.aray_cod_prod = 1
        
    def dados_planilha(self, obj: Produtos):
        dados = [obj.array_cod_prod, obj.array_lote, obj.array_nome_prod, obj.array_quant_result, obj.tamanho_devolucao]
        return dados
        
    def carregar_navegador(self):
        self.driver = webdriver.Chrome()
        pagina = 'https://amberlive.000webhostapp.com/pagina.html'
        self.driver.get(pagina)
    
    def fazer_devolucao(self, tamanho_devolucao: int, array_cod_prod: list, array_lote: list, array_quant_result: list):
            
        #clico no campo Produto
        prod = self.driver.find_element(By.ID, "Product_Name")
        prod.click()
        prod.clear()
        time.sleep(0.2) 

        #digito o codigo e aperto Enter
        prod.send_keys(array_cod_prod[self.linha]+Keys.RETURN)
        time.sleep(0.2)

        #seleciono o botao do endereço de origem
        xpath_orig = '//button[@class="pui-button ui-widget ui-state-default ui-corner-right pui-button-icon-only"]'
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, xpath_orig))
        )
        orig = self.driver.find_elements(By.XPATH, xpath_orig)
        orig[2].click()
        time.sleep(0.2)

        #escolho dentre os elementos (divs) o produto com base no lote
        
        xpath_lote = '//div[@style="padding-left: 10px;margin-top: -10px;" and contains(., "Lote: {}")]'.format(array_lote[self.linha])
        # xpath_lote = "//div[@style='padding-left: 10px;margin-top: -10px;' and contains(., 'Lote: {}')]".format(array_lote[linha])
        # xpath_lote = str("//div[@style=\"padding-left: 10px;margin-top: -10px;\" and contains(., 'Lote: {}')]".format(array_lote[linha]))
        lote = self.driver.find_element(By.XPATH, xpath_lote)
        lote.clear()
        lote.click()

        #escrevo a quantidade certa
        id_quant = self.driver.find_element(By.ID, "Ammount")
        id_quant.clear()
        id_quant.send_keys(array_quant_result[self.linha])

        #clico na posicao da devolucao
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, xpath_lote)), "Erro, xpath nao encontrado {}".format(xpath_lote)
        )
        elemento_posic = self.driver.find_element(By.XPATH, xpath_lote)
        elemento_posic.click()


        #e clico no botao verde
        botao_verde = self.driver.find_element(By.ID, "MovingProduct_Submit")
        botao_verde.click()
        self.linha =+1
        print("Linha: ",self.linha)