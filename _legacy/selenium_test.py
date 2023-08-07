from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from datetime import datetime
from time import sleep
import datetime


USER_ID = "2018111943"
PASSWORD = "asdf8971!@"


driver = webdriver.Chrome()
url="https://sugang.dongguk.edu/"
driver.get(url)

sleep(1)


print("로그인 시도...")

iframes = driver.find_elements(By.CSS_SELECTOR,'iframe')
print("아이프레임 탐색...")
for iframe in iframes:
    print(iframe.get_attribute('name'))
print("아이프레임 탐색완료...")

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"#Main"))

XPATH_ID_INPUT = "/html/body/div[2]/main/div[1]/form/input[1]"
XPATH_PASS_INPUT = "/html/body/div[2]/main/div[1]/form/input[2]"
XPATH_LOGIN_BUTTON = "/html/body/div[2]/main/div[1]/form/button"
driver.find_element(By.XPATH, XPATH_ID_INPUT).send_keys(USER_ID)
driver.find_element(By.XPATH, XPATH_PASS_INPUT).send_keys(PASSWORD)
driver.find_element(By.XPATH, XPATH_LOGIN_BUTTON).click()

sleep(1)
frames = driver.find_elements(By.CSS_SELECTOR,'frame')
print("프레임 탐색...")
for frame in frames:
    print(frame.get_attribute('name'))
print("프레임 탐색완료...")

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"#coreMain"))

print("수강신청 menu로 이동합니다.")

# print(driver.find_element(By.CSS_SELECTOR,'#menu_sugang').get_attribute('onclick'))
driver.execute_script(driver.find_element(By.CSS_SELECTOR,'#menu_sugang').get_attribute('onclick'))

driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,"#coreMain")) #수강신청 버튼이 있는 프레임으로 전환

# iframe 이 load 될때까지 기다려야함 (load 되기 전에는 #btnAddLec 이 없어서 오류)
sleep(1)

print(driver.find_elements(By.CSS_SELECTOR,"#btnAddLec")[0])
driver.find_elements(By.CSS_SELECTOR,"#btnAddLec")[0].click()

print("자동화 소프트웨어가 코드를 전부 실행했습니다...")



while(True):
    pass