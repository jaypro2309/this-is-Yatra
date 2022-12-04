import pytest
import time

from page.flight_results_page import SearchFlightResult
from page.launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerify():
    def test_login_details(self):
        lp = LaunchPage(self.driver, self.wait)
        lp.takeoff("Ahmedabad")
        time.sleep(5)
        lp.land_at("Goa")
        time.sleep(5)
        lp.take_date()
        time.sleep(2)
        lp.selectdate()
        time.sleep(2)
        lp.search()
        time.sleep(2)
        lp.page_scroll()
        sf= SearchFlightResult(self.driver, self.wait)
