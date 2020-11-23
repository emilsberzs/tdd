from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith accidentally tries to submit empty list item,
        # she hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)

        # The home page refreshes, and there is error message stating
        # that list item cannot be empty
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector(
                '.form-group-has-error').text,
            "You can't have an empty list item"
        ))

        # She tries again with some text for the item and now it works
        self.browser.find_element_by_id('id_text').send_keys('Buy milk')
        self.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # She now decides to submit second blank list item
        self.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)

        # She receives similiar warning
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector(
                '.form-group-has-error').text,
            "You can't have an empty list item"
        ))

        # And she can correct it by entering some text in
        self.browser.find_element_by_id('id_text').send_keys('Make tea')
        self.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
