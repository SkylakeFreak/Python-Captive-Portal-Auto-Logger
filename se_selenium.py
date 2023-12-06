import time
import schedule
import time

def roller():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    chrome_driver_path = "C:/Users/utkar/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

    driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path), options=chrome_options)

    try:
        driver.get("http://10.0.0.12:8090/httpclient.html")

        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys("210305105182")
        password_input.send_keys("cd@45")

        login_button = driver.find_element(By.ID, "loginbutton")

        ActionChains(driver).move_to_element(login_button).click().perform()

        time.sleep(5)
        print("Proceeded!")

    finally:
        driver.quit()
        print("Driver quited")

import socket

def check_internet_connection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        print("Internet connection is Live!")
        print("Port Monitoring")
    except (socket.error, OSError):
        print("No internet connection.")
        print("Initiated AutoLogin")
        roller()

#########################
while True:
    check_internet_connection()
    time.sleep(60)


