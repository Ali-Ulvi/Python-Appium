import traceback
from collections import deque

import appium.webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.basepage import basepage
from POM.packPurchase import packPurchase


class Home(basepage):
    LOCATOR_OK = (MobileBy.ID, "mm.com.mptvas:id/dialog_btn_ok")
    LOCATOR_OK_LANG = (MobileBy.ID, "mm.com.mptvas:id/ok_btn")
    LOCATOR_ENGLISH = (MobileBy.ID, "mm.com.mptvas:id/check_english")
    LOCATOR_HAMBURGER = (MobileBy.ID, "mm.com.mptvas:id/home_open_drawer")
    LOCATOR_MAIN_BALANCE = (MobileBy.ID, "mm.com.mptvas:id/balance")
    LOCATOR_BACK = (MobileBy.ID, "mm.com.mptvas:id/back_btn")
    LOCATOR_BACKHOME = (MobileBy.ID, "mm.com.mptvas:id/back_to_home")
    LOCATOR_PACK_PURCHASE = (MobileBy.XPATH, "//*[@text='Package Purchase']")
    LOCATOR_HOME_BUTTON = (MobileBy.XPATH, "//*[@text='Home']")

    def __init__(self, driver: appium.webdriver.Remote) -> object:
        self.driver = driver
        self._stack = deque()

    def switch_to_mpt4u(self):
        self.driver.start_activity("mm.com.mptvas",
                                   'com.ztesoft.zsmart.datamall.app.ui.activity.login.LoginWaitingActivity',
                                   dont_stop_app_on_reset=True)
        return self
    def close_popups(self):

        self.chose_lang()
        self._close_popups(self.LOCATOR_OK)
        return self

    def _close_popups(self,by,wait_seconds=1):
        try:
            WebDriverWait(self.driver, wait_seconds).until(
            EC.visibility_of_element_located((
                by))).click()
        except:
            pass
    def chose_lang(self):
        try:
            WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((
                self.LOCATOR_ENGLISH))).click()
            WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((
                self.LOCATOR_OK_LANG))).click()
        except:
            pass
    def clickPackPurchase(self):
        print("clickPackPurchase")
        super().click(self.LOCATOR_PACK_PURCHASE)
        return packPurchase(self.driver)

    def go_home(self):

        def at_home():
            return self.driver.find_elements_by_id(self.LOCATOR_HAMBURGER[1])

        back_to_home = self.driver.find_elements_by_id(self.LOCATOR_BACKHOME[1])
        if back_to_home:
            back_to_home[0].click()
            return

        try:
            while not at_home():
                self.click(Home.LOCATOR_BACK)
        except Exception:
            print(traceback.format_exc())

    def save_money(self):
        self.go_home()
        self._stack.append(self.get_money())

    def get_money(self):
        self.go_home()
        self.wait_text(self.LOCATOR_MAIN_BALANCE, 'Ks')
        return int(self.getText(Home.LOCATOR_MAIN_BALANCE).strip(" Ks"))

    def check_price(self, expected_price):
        self.save_money()
        actual_prc = (self._stack.pop() - self._stack.pop()) * -1
        assert expected_price == actual_prc, "Actual Price({}Ks) differs from Expected Price({}Ks) ".format(actual_prc, expected_price)
