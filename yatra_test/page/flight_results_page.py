import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configfiles.base_driver import BaseDriver


class SearchFlightResult(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def filter_flight(self):
        self.driver.find_element(By.XPATH,"(//p[@class='font-lightgrey bold'])[2]")
        time.sleep()
        allstops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[text()='32,467']")))
        print(len(allstops1))

        for stop in allstops1:
            print("the text is:" + stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")