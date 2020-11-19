from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith accidentally tries to submit empty list item,
        # she hits Enter on the empty input box

        # The home page refreshes, and there is error message stating
        # that list item cannot be empty

        # She tries again with some text for the item and now it works

        # She now decides to submit second blank list item

        # She receives similiar warning

        # And she can correct it by entering some text in
        self.fail('write me!')
