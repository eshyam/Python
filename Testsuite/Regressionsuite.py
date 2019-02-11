import os
import unittest
from Library.HTMLTestRunner import HTMLTestRunner

from Testscripts.testCaseNo100001 import TestcaseNo100001
from Testscripts.testcaseNo100002 import TestcaseNo100002
from Testscripts.testcaseNo100003 import TestcaseNo100003
from Testscripts.testcaseNo100004 import TestcaseNo100004
from Testscripts.testcaseNo100005 import TestcaseNo100005
from Testscripts.testcaseNo100006 import TestcaseNo100006
from Testscripts.testcaseNo100007 import TestcaseNo100007
from Testscripts.testcaseNo100008 import TestcaseNo100008
from Testscripts.testcaseNo100009 import TestcaseNo100009
from Testscripts.testcaseNo100010 import TestcaseNo100010
from Testscripts.testcaseNo100011 import TestcaseNo100011
from Testscripts.testcaseNo100012 import TestcaseNo100012
from Testscripts.testcaseNo100013 import TestcaseNo100013
from Testscripts.testcaseNo100014 import TestcaseNo100014
from Testscripts.testcaseNo100015 import TestcaseNo100015
from Testscripts.testcaseNo100016 import TestcaseNo100016
from Testscripts.testcaseNo100017 import TestcaseNo100017
from Testscripts.testcaseNo100018 import TestcaseNo100018
from Testscripts.testcaseNo100019 import TestcaseNo100019
from Testscripts.testcaseNo100020 import TestcaseNo100020


dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))


# importing individual test scripts
""" Note: Reason for making individual test scripts - 
As per standard framework guidelines - Each test script should be independent one
"""
suite = unittest.TestSuite()

# Collecting as a suite
suite.addTest(TestcaseNo100001('test_TestcaseNo100001'))
suite.addTest(TestcaseNo100002('test_TestcaseNo100002'))
suite.addTest(TestcaseNo100003('test_TestcaseNo100003'))
suite.addTest(TestcaseNo100004('test_TestcaseNo100004'))
suite.addTest(TestcaseNo100005('test_TestcaseNo100005'))
suite.addTest(TestcaseNo100006('test_TestcaseNo100006'))
suite.addTest(TestcaseNo100007('test_TestcaseNo100007'))
suite.addTest(TestcaseNo100008('test_TestcaseNo100008'))
suite.addTest(TestcaseNo100009('test_TestcaseNo100009'))
suite.addTest(TestcaseNo100010('test_TestcaseNo100010'))
suite.addTest(TestcaseNo100011('test_TestcaseNo100011'))
suite.addTest(TestcaseNo100012('test_TestcaseNo100012'))
suite.addTest(TestcaseNo100013('test_TestcaseNo100013'))
suite.addTest(TestcaseNo100014('test_TestcaseNo100014'))
suite.addTest(TestcaseNo100015('test_TestcaseNo100015'))
suite.addTest(TestcaseNo100016('test_TestcaseNo100016'))
suite.addTest(TestcaseNo100017('test_TestcaseNo100017'))
suite.addTest(TestcaseNo100018('test_TestcaseNo100018'))
suite.addTest(TestcaseNo100019('test_TestcaseNo100019'))
suite.addTest(TestcaseNo100020('test_TestcaseNo100020'))


outfile = file(folder_path + '\Regressionreport\Regressionreport.html', 'w+')
runner = HTMLTestRunner(stream=outfile, verbosity=1, title='Abhibus', description='Regressionreport', dirTestScreenshots =folder_path + '\Screenshots')
runner.run(suite)
outfile.close()

