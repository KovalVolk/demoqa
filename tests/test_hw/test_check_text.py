from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.text_elements.click()
    assert elements_page.equal_url()
    demo_qa_page.text2_elements.click()
    assert elements_page.equal_url()

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()


