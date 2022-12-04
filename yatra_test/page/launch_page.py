import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configfiles.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def takeoff(self, takeoffD):
        take_off = self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_origin_city")))
        take_off.click()
        take_off.send_keys(takeoffD)
        time.sleep(2)
        take_off.send_keys(Keys.ENTER)

    def land_at(self, landatD):
        land_at = self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_arrival_city")))
        land_at.click()
        land_at.send_keys(landatD)
        time.sleep(2)
        land_at.send_keys(Keys.ENTER)

    def take_date(self):
        take_date = self.wait.until(EC.element_to_be_clickable((By.ID, "BE_flight_origin_date")))
        take_date.click()

    def selectdate(self):
        select_date = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//td[@data-date='25/12/2022']")))
        select_date.click()

    def search(self):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_flsearch_btn']")))
        button.click()

