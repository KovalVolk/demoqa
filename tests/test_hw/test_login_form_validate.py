import time

from pages.form_page import FormPage

def test_login_form_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'Email'
    assert form_page.user_email.get_dom_attribute('pattern') == 'Email'

    form_page.first_name.send_keys('')
    form_page.last_name.send_keys('')
    form_page.user_number.send_keys('')

    assert form_page.first_name.get_dom_attribute('class') == 'was-validated'


