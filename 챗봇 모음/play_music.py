import selenium
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

send_music='아이유 celebrity'
def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
    pyperclip.copy(user_input)
    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
    time.sleep(1)
###
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
#options.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver', options=options)
URL = 'https://vibe.naver.com/today'
###
def start():
    driver.get(url=URL)
    driver.implicitly_wait(10)
    login = {
    "id" : "sopo9909",
    "pw" : "hhy3242"
    }
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/a[2]').click()
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[1]/a/span').click()
    driver.implicitly_wait(2)
    clipboard_input('//*[@id="id"]', login.get("id"))
    clipboard_input('//*[@id="pw"]', login.get("pw"))
    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    driver.find_element_by_xpath('//*[@id="header"]/a[1]').click()
def search_music(send_music):
    search = driver.find_element_by_xpath('//*[@id="search_keyword"]')
    search.send_keys(send_music)
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/a').click()
start()
search_music(send_music)