import time
from pages.alerts import Alerts

def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.timerButton.click()
    time.sleep(6)
    assert alert_page.alert()
