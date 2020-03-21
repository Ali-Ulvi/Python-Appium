from appium.webdriver.common.mobileby import MobileBy

from POM.basepage import basepage
from POM.packPurchase2ndPage import packPurchase2ndPage



class packPurchase(basepage):

    #LOCATOR_CARRYPLUS = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.View[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.CheckBox" );

    def __init__(self, driver):
        self.driver = driver


    def clickPurchaseButtonFor(self, pack_name):
        print("clickPurchaseButtonFor "+pack_name)
        #super().click(self.LOCATOR_CARRYPLUS)
        #super().scrollAndClick("Night Time - 7 Nights [800MB]")
        super().scrollAndPurchase(pack_name)
        #super().scrollAndClick("Purchase")
        return packPurchase2ndPage(self.driver)

