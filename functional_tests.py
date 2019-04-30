from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('User peacock feathers to make a fly')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_elements_by_tag_name('tr')

        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        self.assertIn('2: Buy peacock feathers to make a fly', [row.text for row in rows])

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        [...]
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')