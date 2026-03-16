from components.components import WebElement
from pages.base_page import BasePage


class ModalElements(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_menu = WebElement(driver, '#modalWrapper > h1')
        self.icon = WebElement(driver, 'header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')



