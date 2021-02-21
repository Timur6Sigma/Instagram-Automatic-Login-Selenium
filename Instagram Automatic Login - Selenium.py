from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C://Users/Tima6Sigma/Documents/chromedriver_win32/chromedriver")
driver.get("https://instagram.com")

sleep(4)
#Accept cookies from Instagram on this browser?
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
sleep(1)
#Login
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
    .send_keys("Here Username")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
    .send_keys("Here Password")
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button/div")\
    .click()
#Time to put in Google Authentiticator code manual
sleep(20)
#Not now button (Notification activation)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
sleep(3)