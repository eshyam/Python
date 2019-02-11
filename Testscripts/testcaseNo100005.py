from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import os
import traceback
import time

from Syslibrary.datadriver import readjson

jsonread1 = readjson()

from Library.Launchapplication import launchapplication

application = launchapplication()

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

tf = 'test_TestcaseNo100005'


# TestCaseNo:100005


class TestcaseNo100005(unittest.TestCase):
    def test_TestcaseNo100005(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            # abhibus_locator = jsonread1.jsonread(folder_path + '\Object\locators.json')
            abhibus_locator = application.abhibus_locators()
            abhibus_testdata = application.abhibus_testdata()

            # Source
            abhibuspage_origin = browser.find_element(By.ID, abhibus_locator['origin'])
            abhibuspage_origin.send_keys(abhibus_testdata['hyd'])
            time.sleep(2)
            abhibuspage_origin.send_keys(Keys.TAB)

            # Destination
            abhibuspage_destination = browser.find_element(By.ID, abhibus_locator['destination'])
            abhibuspage_destination.send_keys(abhibus_testdata['bang'])
            time.sleep(2)
            abhibuspage_destination.send_keys(Keys.TAB)

            # Onward Journey
            abhibuspage_startdate = browser.find_element(By.XPATH, abhibus_locator['startdate'])
            abhibuspage_startdate.click()

            # Return Journey
            abhibuspage_return_dateofjourney = browser.find_element(By.XPATH, abhibus_locator['returndateofjourney'])
            abhibuspage_return_dateofjourney.click()
            abhibuspage_returndate = browser.find_element(By.XPATH, abhibus_locator['returndate'])
            abhibuspage_returndate.click()

            # Click on Search
            abhibuspage_search_buses = browser.find_element(By.XPATH, abhibus_locator['searchbus'])
            abhibuspage_search_buses.click()
            time.sleep(4)

            # Select onward Travel
            abhibus_travels_onward = browser.find_element(By.XPATH, abhibus_locator['onwardtravels'])
            abhibus_travels_onward.click()
            time.sleep(2)

            # Select Kaveri Travels
            abhibus_kaveri_travels_onward = browser.find_element(By.XPATH, abhibus_locator['kaveritravels'])
            abhibus_kaveri_travels_onward.click()
            time.sleep(2)

            # Select Any Available Bus by Clicking on "Select Seat
            abhibus_selectseat = browser.find_element(By.XPATH, abhibus_locator['selectseat'])
            abhibus_selectseat.click()
            time.sleep(2)

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path + '\Screenshots\Testcae-%s.png' % tf)
            self.fail('Test case No : 100005 is failed')
        finally:
            application.closebrowser(browser)


if __name__ == '__main__':
    unittest.main()


