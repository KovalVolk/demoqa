import time
from pages.tables import Tables


def test_tables(browser):
    pages_tables = Tables(browser)

    pages_tables.visit()
    pages_tables.btn_add.click()

    assert not pages_tables.modal_dialog.exist()
    time.sleep(2)
    pages_tables.first_name.send_keys('tester')
    pages_tables.last_name.send_keys('testerov')
    pages_tables.user_email.send_keys('test@ttt.tt')
    pages_tables.user_age.send_keys('25')
    time.sleep(2)
    pages_tables.btn_submit.click_force()

    assert  pages_tables.modal_dialog.exist()
    assert pages_tables.first_name.get_text()
    assert pages_tables.last_name.get_text()
    assert pages_tables.user_email.get_text()
    assert pages_tables.user_age.get_text()

    pages_tables.btn_pensil.click_force()
    time.sleep(2)
    pages_tables.first_name.send_keys('tester-1')
    time.sleep(2)
    pages_tables.btn_submit.click_force()
    assert pages_tables.first_name.get_text()

    pages_tables.btn_basket.click_force()
    time.sleep(2)
    assert pages_tables.first_name.get_text() == ''
    assert pages_tables.last_name.get_text() == ''
    assert pages_tables.user_email.get_text() == ''
    assert pages_tables.user_age.get_text() == ''


