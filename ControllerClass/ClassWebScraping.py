from selenium import webdriver;
from selenium.webdriver.common.by import By;
from datetime import datetime
import time as time


class ControllerAPI:
	@staticmethod
	def varrerDados(site, url, pathInput, pathBtn, pathTag1, pathTag2=None):
		try:
			print('Varrer')
			driver = webdriver.Remote("http://localhost:4444", options=webdriver.ChromeOptions())
			#options = webdriver.ChromeOptions()
			#options.add_argument("--headless=new")
			#driver = webdriver.Chrome(options=options)
			#driver = webdriver.Firefox()
			driver.get(url)
			driver.implicitly_wait(5) 
			data_e_hora_atuais = datetime.now()
			data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
			print(f'{site} {data_e_hora_em_texto}')
			driver.execute_script(f'document.querySelector("input").value = {site}')
			driver.implicitly_wait(5) 
			#xpathInput = driver.find_element(By.XPATH, pathInput)
			xpathbtn = driver.find_element(By.XPATH, pathBtn).click()
			xpathDataEnd1 = driver.find_element(By.XPATH, pathTag1)
			if pathTag2 != "":
				xpathDataEnd2 = driver.find_element(By.XPATH, pathTag2)
				return [xpathDataEnd1.text, xpathDataEnd2.text]
			elif pathTag2 == "":
				return xpathDataEnd1.text
			
		except:
			return f'Sem acesso ao Site {site}'
		
		finally:
			driver.quit()
		