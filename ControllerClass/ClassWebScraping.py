from selenium import webdriver;
from selenium.webdriver.common.by import By;
from datetime import datetime
import time as time

from BaseData.exec import OperatorClass

class ControllerAPI:
	@staticmethod
	def varrerDados(site = None, url = None, pathInput = None, pathBtn = None, pathTag = None):
		try:
			print('Varrer')
			#options = webdriver.ChromeOptions()
			#options.add_argument("--headless=new")
			#driver = webdriver.Chrome(options=options)
			driver = webdriver.Firefox()
			driver.get(url)
			driver.maximize_window() #ABRE COM A JENALA FULL
			driver.implicitly_wait(5) 
			#BARRA LATERAL AUTO SCROLL
			scroll = driver.execute_script('return document.body.scrollHeight')
			for contador in range(200):
				driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
				time.sleep(2)
				new_scroll = driver.execute_script('return document.body.scrollHeight')
				if new_scroll == scroll:
					break
				scroll = new_scroll

			data_e_hora_atuais = datetime.now()
			data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
			print(f'{site} {data_e_hora_em_texto}')
			driver.execute_script(f'document.querySelector("input").value = {site}')
			driver.implicitly_wait(5) 
			#xpathInput = driver.find_element(By.XPATH, pathInput)
			xpathbtn = driver.find_element(By.XPATH, pathBtn).click()
			xpathData = driver.find_element(By.XPATH, pathTag)
			print(xpathData.text)
			return OperatorClass.write(site, xpathData.text)	
		except:
			return f'Sem acesso ao Site {site}'
		
