from pages.modal_dialogs import ModalElements
from components.components import WebElement
import time
from pages.demoqa import DemoQa



def test_modal_elements(browser):
    modal_elements = ModalElements(browser)
    modal_elements.visit()

    assert modal_elements.btns_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    demo_qa_page = DemoQa(browser)
    modal_elements = ModalElements(browser)
    modal_elements.visit()
    modal_elements.refresh()

    modal_elements.icon.click()
    browser.back()

    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forvard()

    assert  demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)







