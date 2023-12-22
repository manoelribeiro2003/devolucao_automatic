from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://10.250.1.8:8090")
elem = driver.find_element(By.ID, "Login")
elem.send_keys("0028")
elem = driver.find_element(By.ID, "Password")
elem.send_keys("Claudiane.1")
elem.send_keys(Keys.RETURN)
elem.find_element(By.XPATH, "//*[text()='Processos Internos']")
elem.click()

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
