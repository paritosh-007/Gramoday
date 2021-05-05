from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def download(url):
	try:
		driver=webdriver.Firefox(executable_path='G:/geckodriver-v0.24.0-win64/geckodriver.exe')	
		
		driver.get(url)
		
		xpath='//*[@id="cphBody_ButtonExcel"]'
			   
		element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

		element.click()
		
		
		
		
	except:
		print(url+'error')
		pass		
	

def main():
	download('https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom=01-Jan-2020&DateTo=31-Dec-2020&Fr_Date=01-Jan-2020&To_Date=31-Dec-2020&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--')
			
			

if __name__=="__main__":
	main()