from selenium.webdriver.common.by import By
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

tf = 'test_TestcaseNo100001'


# TestcaseNo:100001


class TestcaseNo100001(unittest.TestCase):
    def test_TestcaseNo100001(self):
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            # abhibus_locator = jsonread1.jsonread(folder_path + '\Object\locators.json')
            abhibus_locator = application.abhibus_locators()
            abhibus_testdata = application.abhibus_testdata()

            # Abhibus Logo Tooltip Validation
            abhibuspage_logo_tooltip = browser.find_element(By.XPATH, abhibus_locator['logo'])
            abhibuspage_logo_tooltip = abhibuspage_logo_tooltip.get_attribute("title")
            print(abhibuspage_logo_tooltip)
            time.sleep(3)
            self.assertEqual(abhibuspage_logo_tooltip, "abhibus.com - India's Fastest Online bus ticket booking site")



        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path + '\Screenshots\Testcae-%s.png' % tf)
            self.fail('Test case No : 100001 is failed')
        finally:
            application.closebrowser(browser)


if __name__ == '__main__':
    unittest.main()


