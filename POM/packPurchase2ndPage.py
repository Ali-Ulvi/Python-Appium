from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from POM.basepage import basepage
from POM.packPurchaseLastPage import PackPurchaseLastPage



class packPurchase2ndPage(basepage):
    LOCATOR_OFFER_NAME = (By.ID, "mm.com.mptvas:id/offer_name")
    LOCATOR_YES = (By.ID, "mm.com.mptvas:id/dialog_yes_btn")
    LOCATOR_PURCHASE = (By.ID, "mm.com.mptvas:id/submit")

    def __init__(self, driver):
        self.driver = driver

    def assertOfferName(self, text):
        assert text == super().getText(self.LOCATOR_OFFER_NAME), "Offer Name Incorrect in packPurchase2ndPage. Expected: " + text + " Actual: " + super().getText(self.LOCATOR_OFFER_NAME)
        return self
    def purchase(self):
        self.click(self.LOCATOR_PURCHASE)
        return self
    def yes(self):
        self.click(self.LOCATOR_YES)
        return PackPurchaseLastPage(self.driver)
