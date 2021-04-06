from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

try:
    driver.get("https://orteil.dashnet.org/cookieclicker")

    cookie = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    count = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "cookies"))
    )
    items = [WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "product0"))),
            WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "product1")))]

    actions = ActionChains(driver)
    actions.click(cookie)

    for i in range(5000):
        actions.perform()
        num = int(count.text.split(" ")[0])
        for item in items:
            value = int(item.text.split("\n")[1])
            if value < num:
                act = ActionChains(driver)
                act.move_to_element(item)
                act.click()
                act.perform()
finally:
    time.sleep(5)
    driver.quit()

# # driver.get("https://superbet.ro")
# # driver.get("https://superbet.ro/wiki/bonus-de-bun-venit-sport")
# driver.get("https://www.techwithtim.net/")
#
# print(driver.title)
#
# # search = driver.find_element_by_name("search-box")
# # search = driver.find_element_by_name("s")
# # search.send_keys("test")
# # search.send_keys(Keys.RETURN)
#
# try:
#     # main = WebDriverWait(driver, 5).until(
#     #     EC.presence_of_element_located((By.ID, "main"))
#     # )
#     # print(main.text)
#     #
#     # articles = main.find_element_by_tag_name("article")
#     # for article in articles:
#     #     header = article.find_element_by_name("entry-summary")
#     #     print("header")
#
#     link = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
#     )
#     link.click()
#     print(driver.title)
#
#     link = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     link.click()
#     print(driver.title)
#
#     time.sleep(5)
#     driver.back()
#     driver.back()
#     driver.forward()
#
# finally:
#     time.sleep(5)
#     driver.quit()


