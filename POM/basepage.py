from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import Remote


class basepage(object):

    def __init__(self, driver: Remote):
        self.driver = driver

    def click(self, by):
        WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located((
                by)))
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((
                by))).click()

    def wait_invisible(self, by):
        WebDriverWait(self.driver, 18).until(
            EC.invisibility_of_element_located((
                by)))
    def wait_visible(self, by):
        WebDriverWait(self.driver, 28).until(
            EC.visibility_of_element_located((
                by)))

    def wait_text(self, by, text):
        WebDriverWait(self.driver, 18).until(
            EC.text_to_be_present_in_element(
                by, text))

    def scrollAndClick(self, text, i=7):
        while i > 0:
            try:
                self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(" + "new UiSelector().text(\"" + text + "\"));").click()
                break
            except Exception:
                i -= 1
    def scrollAndPurchase(self, text, i=7):
        pack=None
        while i > 0:
            try:
                pack=self.driver.find_element_by_android_uiautomator(
                    "new UiScrollable(new UiSelector()).scrollIntoView(" + "new UiSelector().text(\"" + text + "\"));")
                pack.click()

                break
            except Exception:
                i -= 1

        self.driver.scroll(pack,self.driver.find_element_by_id("mm.com.mptvas:id/data_bundle"),2600)
        text='Purchase'
        sleep(1)

        self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()).scrollIntoView(" + "new UiSelector().text(\"" + text + "\"));").click()
           # find_element_by_xpath("parent::*/parent::*/parent::*/parent::*/android.widget.TextView[2]").click()
    def getText(self, by) -> str:
        return WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((
                by))).text
