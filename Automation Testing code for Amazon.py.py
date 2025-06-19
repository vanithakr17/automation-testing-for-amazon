import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

driver=webdriver.Firefox() 

 #getting into the website
driver.get("https://www.amazon.in")  
 #for maximize the window                                         
driver.maximize_window()   

 #input xpath of the searchbox to click                                                    
searchbox=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')       
searchbox.click()
searchbox.send_keys("tv")
searchbox.send_keys(Keys.RETURN)
time.sleep(3)

 #to scroll the website
driver.execute_script("window.scrollBy(0,500);")                              
time.sleep(3)

 #to randomly click the product
tv=driver.find_elements(By.XPATH,'//*[@id="a-autoid-4-announce"]')            
if tv:
    tv1=random.choice(tv)
    tv1.click()
else:
    print("no response")
time.sleep(3)    

 #go to cart
gotocart=driver.find_element(By.XPATH,'//*[@id="nav-cart-count"]')
gotocart.click()
time.sleep(3)

 #proceed to buy
proceedtobuy=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div[5]/div/div[1]/div[1]/div/form/div/div[3]/span[1]/span/span/input')
proceedtobuy.click()
time.sleep(3)

 #to enter mobile number
enternumber=driver.find_element(By.XPATH,'//*[@id="ap_email_login"]')
enternumber.click()
enternumber.send_keys('9080837115')
enternumber.send_keys(Keys.RETURN)
time.sleep(3)

 #to enter password
password=driver.find_element(By.XPATH,'//*[@id="ap_password"]')
password.click()
password.send_keys('vani2005')
password.send_keys(Keys.RETURN)
time.sleep(3)
