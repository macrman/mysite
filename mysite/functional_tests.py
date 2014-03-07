from splinter import Browser
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
       self.browser = Browser('firefox') 

    def tearDown(self):
        self.browser.quit()

    def test_visit_site_and_read_posts(self):
        # Tom visits our homepage, see's it's my site
        self.browser.visit('http://localhost:8000')
        self.assertTrue(self.browser.is_text_present('mac'))
        # he see's a list of posts, clicks the first one
        note_links = Browser.find_by_css('#note_link')
        note_links[0].click() #maybe verifiy it goes to correct link?
        # verify url?
        # he finishes reading, then goes to sleep

if __name__ == '__main__':
    unittest.main()
