import time
from pages.tables import Tables


def test_tables(browser):
    pages_tables = Tables(browser)

    pages_tables.visit()
    pages_tables.first_name.click()
    assert pages_tables.first_name.get_dom_attribute('placeholder') == 'First Name'

    pages_tables.last_name.click()
    assert pages_tables.last_name.get_dom_attribute('placeholder') == 'last Name'

    pages_tables.user_age.click()
    assert pages_tables.user_age.get_dom_attribute('placeholder') == 'User Age'

    pages_tables.user_email.click()
    assert pages_tables.user_email.get_dom_attribute('placeholder') == 'User Email'
