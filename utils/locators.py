from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SUBMIT_BUTTON = (By.XPATH, '//input[@class="btn btn-success"]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@class="alert alert-success alert-dismissible"]')
