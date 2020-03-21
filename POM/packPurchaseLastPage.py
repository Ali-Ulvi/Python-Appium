from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from POM.basepage import basepage



class PackPurchaseLastPage(basepage):
    LOCATOR_OFFER_NAME = (By.ID, "mm.com.mptvas:id/offer_name")
    LOCATOR_YES = (By.ID, "mm.com.mptvas:id/dialog_yes_btn")
    LOCATOR_SUCCESS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView[1]")

    def __init__(self, driver):
        self.driver = driver

    def assertSuccessText(self):
        self.wait_visible((MobileBy.XPATH,"//*[@text='Purchase Success !']"))
        return self