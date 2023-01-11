import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

GUAR_DOWN = 150
GUAR_UP = 5
chrome_driver_path = ""



class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(15)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        while self.down == "--" or self.up == "--":
            time.sleep(2)
            self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
            self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.up = float(self.up)
        self.down = float(self.down)
        print(f"down: {self.down}")
        print(f"up: {self.up}")


bot = InternetSpeedTwitterBot(chrome_driver_path)

bot.get_internet_speed()
