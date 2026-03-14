import time
from pages.text_box import TextBox

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()

    text_box.full_name.send_keys('tester')
    text_box.current_address.send_keys('text')

    time.sleep(2)
    text_box.btn_submit.click_force()
    assert text_box.full_name.get_text()
    assert text_box.current_address.get_text()



