import time
from pages.modal_dialogs import ModalElements



def test_check_modal(browser):
    modal_elements = ModalElements(browser)
    modal_elements.visit()


    modal_elements.small_modal.click()
    time.sleep(2)
    assert modal_elements.alert()
    modal_elements.close_small_modal.click()
    time.sleep(2)
    assert not modal_elements.alert()

    modal_elements.large_modal.click()
    time.sleep(2)
    assert modal_elements.alert()
    modal_elements.close_large_modal.click()
    time.sleep(2)
    assert not modal_elements.alert()

