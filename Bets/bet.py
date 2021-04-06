from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 5)

try:
    driver.get("https://superbet.ro/pariuri-sportive/fotbal/astazi")
    driver.implicitly_wait(2)
    # driver.back()
    # search = wait.until(EC.presence_of_element_located((By.ID, "search-box")))
    driver.implicitly_wait(1)
    elements = driver.find_elements_by_class_name("group-header__wrapper has-market-filters markets-optimized--3")
    print(len(elements))
    for i, element in enumerate(elements):
        try:
            teams = element.find_element_by_class_name("event-summary")
            cote = element.find_element_by_class_name("event-row___markets")
            print(f"\n{i}\n", *teams.text.split("\n")[2:4], *cote.text.split("\n")[1:8:3])
        except:
            print(f"\n{i}\n")
        # try:
        #     names = teams.find_elements_by_class_name("event-summary__score-wrapper")
        #     print(f"\n{i}\n", names.text)
        # except:
        #     print("not")
    print(driver.title)
finally:
    time.sleep(5)
    driver.quit()

