import time
from pages.tables import Tables


def test_tables(browser):
    pages_tables = Tables(browser)

    pages_tables.visit()
    assert not pages_tables.no_data.exist()

    while pages_tables.btn_delete_row.exist():
        pages_tables.btn_delete_row.click()

    time.sleep(2)
    assert pages_tables.no_data.exist()
