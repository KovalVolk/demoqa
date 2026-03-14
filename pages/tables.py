from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '##addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.user_age = WebElement(driver, '#userAge')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, '#body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.btn_pensil = WebElement(driver, '#root > div > div > div > div.col-12.mt-4.col-md-3.col-xl-3')
        self.btn_basket = WebElement(driver, '#root > div > div > div > div.col-12.mt-4.col-md-3.col-xl-3')

