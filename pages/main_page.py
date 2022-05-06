from selenium import webdriver

from utils.locators import MainPageLocators


class MainPage():


    def __init__(self, driver):
        self.driver = driver
        self.locator = MainPageLocators

    def click_on_submit_button(self):
        self.driver.find_element(*self.locator.SUBMIT_BUTTON).click()

    def is_success_message_visible(self):
        success_message = self.driver.find_element(*self.locator.SUCCESS_MESSAGE)
        return success_message.is_displayed()


