from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from datetime import datetime
from time import sleep
import datetime

txt_filename = __file__[__file__.find('browser'):__file__.find('browser')+8]+".txt"

def timer(myTime):
    while(True):
        now = datetime.datetime.now()
        print(f"버튼:{BTN_IDX} 목표시간:{TARGET_TIME} 남은시간:{TARGET_TIME-now}")
        # print(myTime)
        # print(now==target_time)
        if(now>myTime):
            print("작동!")
            break

try:
    with open(txt_filename,'r',encoding='utf-8') as file:
        content = file.read().split('\n')
        USER_ID=content[0]
        PASSWORD=content[1]
        ts = content[3].split(':') # 2023:8:7:18:49:15:999999
        its = list(map(int,ts))
        TARGET_TIME=datetime.datetime(its[0], its[1], its[2], its[3], its[4], its[5], its[6])
        BTN_IDX=int(content[4])
except Exception as e:
    print(e)
    pass

try:
    with open(txt_filename,'r',encoding='cp949') as file:
        content = file.read().split('\n')
        content = file.read().split('\n')
        USER_ID=content[0]
        PASSWORD=content[1]
        ts = content[2].split(':') # 2023:8:7:18:49:15:999999
        its = list(map(int,ts))
        TARGET_TIME=datetime.datetime(its[0], its[1], its[2], its[3], its[4], its[5], its[6])
        BTN_IDX=int(content[3])
        
except Exception as e:
    print(e)
    pass

sleep(1)

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
print(f"매크로가 누를 버튼 번호(위에서부터 1~8) : {BTN_IDX}")
print(f"매크로가 버튼을 누르는 시간 : {TARGET_TIME}")
timer(TARGET_TIME)
try:
    print(driver.find_elements(By.CSS_SELECTOR,"#btnAddLec")[BTN_IDX])
    driver.find_elements(By.CSS_SELECTOR,"#btnAddLec")[BTN_IDX].click()
except Exception as e:
    print("해당 버튼이 없거나, 오류가 발생했습니다.")
    print(e)

print("자동화 소프트웨어가 코드를 전부 실행했습니다...")

while(True):
    pass