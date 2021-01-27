from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FlipKart():
    def test(self):
        baseUrl = "https://flipkart.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Enter Credentials
        userName = usr_name = driver.find_element_by_css_selector("input[Class='_2IX_2- VJZDxU']")
        userName.send_keys("Provide your Id or Phone Number")

        password = driver.find_element_by_css_selector("input[Class='_2IX_2- _3mctLh VJZDxU']")
        password.send_keys("Provide Your Password")

        # Click on Login button
        login = driver.find_element_by_css_selector("button[Class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        print("Login Successful !!!")
        time.sleep(3)
        # Find parent Handle
        parentHandle = driver.current_window_handle
        print("Parent Handle is : " + parentHandle)

        # Search for available Selenium books
        searchName = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
        searchName.send_keys("Selenium Book")
        clickSearch = driver.find_element(By.XPATH, "//button[@type='submit']")
        clickSearch.click()

        # Select First Book
        time.sleep(5)
        firstBook = driver.find_element(By.XPATH, "(//a[contains(text(), 'Selenium')])[1]")
        firstBook.click()

        # Find all handles, there should be two handles after clicking Book Link
        handles = driver.window_handles
        print("Handless are : ", handles)

        # Switch to Tab
        for handle in handles:
            print("Handle is : " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to Handle : " + handle)
                time.sleep(3)
                addToCart = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']")
                addToCart.click()


f = FlipKart()
f.test()
