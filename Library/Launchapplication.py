"""
All the classes and corresponding functions will be here, all the functions are reusable components.
These functions are loosely coupled so anyone can make use of them anytime.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import sys

# Getting Current Working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))
# Getting Parent of Current Working Folder
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
# Navigating to desired folder
sys.path.insert(0, folder_path + "\Syslibrary")

# Importing module from Syslibrary
from Syslibrary.datadriver import readjson

# Creating class object and instance of that object
jsonread1 = readjson()


class launchapplication():
    def intializebrowser(self):
        env =jsonread1.jsonread(folder_path + '\Env\setup.json')
        if env['browser'] == 'chrome':
            # browser = webdriver.Chrome(folder_path + '\Env\chromedirver.exe')
            browser = webdriver.Chrome()
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'firefox':
            # browser = webdriver.Firefox(folder_path + '\Env\geckodriver.exe')
            browser = webdriver.Firefox()
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'headlessChrome':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size = 1920x1080")
            chrome_driver = folder_path + '\Env\chromedriver.exe'
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
            browser.implicitly_wait(10)
            return browser

    def closebrowser(self, browser):
        browser.close()

    def inputurl(self, browser):
        url = jsonread1.jsonread(folder_path + '\Env\setup.json')
        if url['url'] == 'prestagurl':
            prestagurl = jsonread1.jsonread(folder_path + '\Env\setup.json')
            browser.get(prestagurl['prestagurl'])

        elif url['url'] == 'stagurl':
            stagurl = jsonread1.jsonread(folder_path + '\Env|setup.json')
            browser.get(stagurl['stagurl'])

    def abhibus_locators(self):
        abhibus_locators = jsonread1.jsonread(folder_path + '\Object\locators.json')
        return abhibus_locators

    def abhibus_testdata(self):
        abhibus_testdata = jsonread1.jsonread(folder_path + '\Data\Testdata.json')
        return abhibus_testdata

    def abhibus_originsourcehyd(self, browser, abhibus_locators):
        origin = browser.fin_element(By.ID, abhibus_locators['origin'])
        return origin





