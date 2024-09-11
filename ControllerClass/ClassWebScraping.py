from selenium import webdriver;
from selenium.webdriver.common.by import By;
from datetime import datetime
import time as time

from BaseData.exec import OperatorClass

class ControllerAPI:
	def __init__(self, site, url, pathInput, pathBtn, pathTag1, pathTag2=None):
		self.site = site
		self.url = url
		self.pathInput = pathInput
		self.pathBtn = pathBtn
		self.pathTag1 = pathTag1
		self.pathTag2 = pathTag2
	def verificarDados(self):
		valor = OperatorClass.read(data=self.site)
		if valor:
			return valor
		else:
			return self.__varrerDados()
			
	def __varrerDados(self):
		try:
			print('Varrer')
			#options = webdriver.ChromeOptions()
			#options.add_argument("--headless=new")
			#driver = webdriver.Chrome(options=options)
			driver = webdriver.Firefox()
			driver.get(self.url)
			driver.implicitly_wait(5) 
			data_e_hora_atuais = datetime.now()
			data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
			print(f'{self.site} {data_e_hora_em_texto}')
			driver.execute_script(f'document.querySelector("input").value = {self.site}')
			driver.implicitly_wait(5) 
			#xpathInput = driver.find_element(By.XPATH, pathInput)
			xpathbtn = driver.find_element(By.XPATH, self.pathBtn).click()
			xpathDataEnd1 = driver.find_element(By.XPATH, self.pathTag1)
			if self.pathTag2 != "":
				xpathDataEnd2 = driver.find_element(By.XPATH, self.pathTag1)
				return OperatorClass.write(self.site, f"[{xpathDataEnd1.text}, {xpathDataEnd2.text}]")
			elif self.pathTag2 == "":
				xpathDataEnd1 = driver.find_element(By.XPATH, self.pathTag1)
				OperatorClass.write(self.site, xpathDataEnd1.text)
				print(self.site)
				return OperatorClass.read(data=self.site)
			driver.quit()
		except:
			return f'Sem acesso ao Site {self.site}'
		