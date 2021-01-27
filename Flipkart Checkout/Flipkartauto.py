from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://flipkart.com")
usr_name = driver.find_element_by_css_selector("input[Class='_2IX_2- VJZDxU']")
usr_name.send_keys("Provide Your Flipkart Login ID/Phone No.")
pswd = driver.find_element_by_css_selector("input[Class='_2IX_2- _3mctLh VJZDxU']")
pswd.send_keys("Provide your Flipkart password")
time.sleep(2)
driver.find_element_by_css_selector("button[Class='_2KpZ6l _2HKlqd _3AWRsL']").click()
time.sleep(2)
driver.find_element_by_css_selector("input[class='_3704LK']").send_keys("Apple iPad" + Keys.ENTER)
parenthandle = driver.current_window_handle
print(parenthandle)
time.sleep(3)
driver.find_element_by_xpath("(//a[contains(text(),'Apple iPad')])[1]").click()
time.sleep(5)
handles = driver.window_handles
for handle in handles:
    print("handle:" + handle)
    if handle not in parenthandle:
        driver.switch_to.window(handle)
        print(driver.current_window_handle)
        driver.find_element_by_css_selector("button[class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']").click()
        time.sleep(15)
        driver.find_element_by_css_selector("button[class='_2KpZ6l RLM7ES _3AWRsL']").click()
        time.sleep(4)
        driver.find_element_by_css_selector("button[class='_2KpZ6l _1seccl _3AWRsL']").click()
        time.sleep(5)
        driver.close()
driver.quit()
