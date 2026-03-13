from components.components import WebElement
from pages.base_page import BasePage

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_content = WebElement(driver, '#section1Content > p')
        self.section_heading = WebElement(driver, '#section1Heading')
        self.section1_content = WebElement(driver, 'p:nth-child(1)')
        self.section2_content = WebElement(driver, 'p:nth-child(2)')
        self.section3_content = WebElement(driver, 'p')

