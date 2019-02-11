from selenium.webdriver.common.by import By
import unittest
import os
import traceback

from Syslibrary.datadriver import readjson
jsonread1 = readjson()

from Library.Launchapplication import launchapplication
application = launchapplication()

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

tf = 'test_TestcaseNo100002'

# TestCaseNo:100001


class TestcaseNo100002(unittest.TestCase):
    def test_TestcaseNo100002(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            # abhibus_locator = jsonread1.jsonread(folder_path + '\Object\locators.json')
            abhibus_locator = application.abhibus_locators()
            abhibus_testdata = application.abhibus_testdata()

            # Source Validation
            abhibuspage_origin = browser.find_element(By.ID, abhibus_locator['origin'])
            abhibuspage_origin.send_keys(abhibus_testdata['hyd'])
            abhibuspage_origin = browser.find_element(By.XPATH, abhibus_locator['Hyd'])

            self.assertEqual(abhibuspage_origin.text, 'Hyderabad')

            # Destination Validation
            abhibuspage_destination = browser.find_element(By.ID, abhibus_locator['destination'])
            abhibuspage_destination.send_keys(abhibus_testdata['bang'])
            abhibuspage_destination = browser.find_element(By.XPATH, abhibus_locator['Bang'])

            self.assertEqual(abhibuspage_destination.text, 'Bangalore')

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path + '\Screenshots\Testcae-%s.png' % tf)
            self.fail('Test case No : 100002 is failed')
        finally:
            application.closebrowser(browser)


if __name__ == '__main__':
    unittest.main()


