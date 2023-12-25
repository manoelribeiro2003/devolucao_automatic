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
        
    def contador(self):
        self.linha = self.linha + 1
        
    def dados_planilha(self, obj: Produtos):
        dados = [obj.array_cod_prod, obj.array_lote, obj.array_nome_prod, obj.array_quant_result, obj.tamanho_devolucao]
        return dados
        
    def carregar_navegador(self):
        self.driver = webdriver.Chrome()
        pagina = 'https://amberlive.000webhostapp.com/pagina.html'
        self.driver.get(pagina)
    
    def fazer_devolucao(self, array_cod_prod: list, array_lote: list, array_quant_result: list):
            
        # Localizo o RadioButton de Devolucao ✓
        bot_dev = self.driver.find_element(By.ID, "OriginalAddress_Devolution")
        # Clico nesse botão ✓
        bot_dev.click()
        # E espero um pouco ✓
        time.sleep(0.2)
        #---------------------------------------------------------------------------------------------------------
        
        # Localizo o campo input de produtos ✓
        prod = self.driver.find_element(By.ID, "Product_Name")
        # Clico nesse input ✓
        prod.click()
        # Limpo esse input, para evitar qualquer coisa ✓
        prod.clear()
        # E espero um pouco ✓
        time.sleep(0.2)
        # Digito o codigo do produto ✓
        prod.send_keys(array_cod_prod[self.linha])
        #
        # Caso não queira usar o WebDriver Wait: time.sleep(3)
        #
        # ANALISAR SE NÃO SERIA MELHOR ESCREVER O CÓDIGO E TAMBÉM O NOME: prod.send_keys(array_cod_prod[self.linha], " - ", array_nome_prod[linha])
        #
        # WebDriver Wait para esperar aparecer o produto na pesquisa
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "xpath do produto que aparecer"))
        )
        #
        # Talvez assim seja mais facil
        # if ('elemento nao apareceu'):
        #   break    
        #
        #Elemento apareceu? Então aperta Enter
        prod.send_keys(Keys.RETURN)        
        #---------------------------------------------------------------------------------------------------------
        
        
        #
        # -> Olhar melhor o xpath desses botões (saber se é realmente esse, porque exitiam 2 botões de cada no site offline)
        #
        # Xpath dos botões Dropdowns
        xpath_dropdowns = '//button[@class="pui-button ui-widget ui-state-default ui-corner-right pui-button-icon-only"]'
        # Pego a lista dos botões dropdown
        list_bot_drop = self.driver.find_elements(By.XPATH, xpath_dropdowns)
        # Clico no 2º botão dropdown (botão do endereço de origem da devolução) ✓
        list_bot_drop[1].click()
        #---------------------------------------------------------------------------------------------------------

        
        # Xpath da DIV que contem o lote do produto a ser devolvido
        xpath_div_lote = '//div[@style="padding-left: 10px;margin-top: -10px;" and contains(., "Lote: {}")]'.format(array_lote[self.linha])
        # WebDriver Wait para esperar aparecer a DIV do produto a ser devolvido
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, xpath_div_lote))
        )
        # Apareceu? Então localizo essa DIV
        div_prod = self.driver.find_element(By.XPATH, xpath_div_lote)
        # Clico nessa DIV
        div_prod.click()
        # e espero um pouco
        time.sleep(0.2)
        #---------------------------------------------------------------------------------------------------------

        # Localizo o input de quantidades ✓
        id_quant = self.driver.find_element(By.ID, "Ammount")
        # Clico nesse input ✓
        id_quant.click()
        #Limpo o input ✓
        id_quant.clear()
        # Espero um pouco ✓
        time.sleep(0.2)
        # Digito a quantidade certa ✓
        id_quant.send_keys(array_quant_result[self.linha])
        #---------------------------------------------------------------------------------------------------------

        #
        # ANALIZAR NA HR O MELHOR XPATH PARA A POSIÇÃO 
        # (PROVAVEL QUE SERÁ PARECIDO COM OS ELEMENTOS DE DIVs NO TRECHO DE CÓDIGO ACIMA)
        #
        # Clico no 3º botão dropdown (endereço de destino)
        list_bot_drop[2].click()
        # Xpath da DIV do endereço de devolução
        xpath_div_dev = 'xpath_div_dev'
        # WebDriver Wait para esperar aparecer a (provavel) DIV do endereço de destino
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, xpath_div_dev))
        )
        # Apareceu? Então localizo essa DIV
        div_dev = self.driver.find_element(By.XPATH, xpath_div_dev)
        # E clico nessa DIV que aparecer
        div_dev.click()
        #---------------------------------------------------------------------------------------------------------

        # Localizo o botao verde ✓
        botao_verde = self.driver.find_element(By.ID, "MovingProduct_Submit")
        # Clico no botão verde ✓
        botao_verde.click()
        # Adiciono +1 á linha ✓
        self.contador()