from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# options = uc.ChromeOptions()
# path = r'C:\Users\Karachi Computer\AppData\Local\Google\Chrome\User Data\Profile 2'
# options.add_argument(fr"user-data-dir={path}")
# #options.add_argument(f'--profile-directory=Profile 14')
# driver = uc.Chrome(options=options)
PATH = "chromedriver.exe"

options = Options()
options.add_argument("--user-data-dir=C:/Users/Umar/AppData/Local/Google/Chrome/User Data/Default")
#options.add_argument("profile-directory=Profile 3")

driver = webdriver.Chrome(PATH,options=options)
driver.implicitly_wait(7)
driver.maximize_window()
# # actionChains = ActionChains(driver)
driver.get("https://www.freepik.com/author/dailytransport882")  # Go to website
while True:
    links_ele = driver.find_elements(By.XPATH,
                                        "//div[@class='showcase__content tags-links']/a")

    links = [single.get_attribute("href") for single in links_ele]
    for single in links:
        driver.get(single)
        sleep(5)
        #input()
        #//aside/div/div/div/div/button[2]
        wait = WebDriverWait(driver, 10)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/aside/div[1]/div/div/div[1]/a/span[1]')))
        driver.execute_script("arguments[0].click();", download_button)
        sleep(2)
        #download_link = [l.get_attribute("href")]
        #for l in download_link:
         #   driver.get(l)
    sleep(40)
       # input()
   