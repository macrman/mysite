from splinter import Browser
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
       self.browser = Browser('firefox') 

    def tearDown(self):
        self.browser.quit()

    # Jen visits our homepage, see's it's my site
    def test_visit_homepage(self):
        self.browser.visit('http://localhost:8000')
        self.assertTrue(self.browser.is_text_present('Django'))
    #   self.fail('finished test')

    # Jen sees that there are no posts from me goes away

    # Tom visits the site, see's my branding
    # he see's a list of posts, clicks the first one
    # he finishes reading, then goes to sleep

if __name__ == '__main__':
    unittest.main()
