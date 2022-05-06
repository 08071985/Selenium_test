import unittest
from base_test import BaseTest
from pages.main_page import MainPage


class TestSignInPage(BaseTest):

    def test_sign_up_button(self):
        page = MainPage(self.driver)
        page.click_on_submit_button()
        self.assertTrue(page.is_success_message_visible())