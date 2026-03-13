import time
from pages.accordion import Accordion

def test_page_accordion(browser):
    accord_page = Accordion(browser)

    accord_page.visit()
    assert accord_page.section_content.visible()

    accord_page.section_heading.click()
    time.sleep(2)
    assert not accord_page.section_content.visible()

def test_visible_accordion_default(browser):
    accord_page = Accordion(browser)
    accord_page.visit()

    assert accord_page.section1_content.visible()
    accord_page.section1_content.click()
    time.sleep(2)
    assert not accord_page.section1_content.visible()

    assert accord_page.section2_content.visible()
    accord_page.section2_content.click()
    time.sleep(2)
    assert not accord_page.section2_content.visible()

    assert accord_page.section3_content.visible()
    accord_page.section3_content.click()
    time.sleep(2)
    assert not accord_page.section3_content.visible()

