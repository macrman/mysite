from splinter import Browser
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
       self.browser = Browser('firefox') 

    def tearDown(self):
        self.browser.quit()

    def test_visit_homepage(self):
        self.browser.visit('http://localhost:8000')
        self.assertTrue(self.browser.is_text_present('Django'))
        self.fail('finished test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
