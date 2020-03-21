import unittest
import datetime
import allure
from allure_commons.types import AttachmentType

from POM.home import Home
from POM.sms import Sms
from actions.purchase_pack import PurchasePack

from test.basetest import basetest

driver_global = None


def decorator_screenshot(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            allure.attach(driver_global.get_screenshot_as_png(), "Screenshot", AttachmentType.PNG)
            raise

    return wrapper


class test_MPT4U(unittest.TestCase):

    def setUp(self):
        global driver_global
        self.base = basetest()
        self.driver = driver_global = self.base.driver

    @decorator_screenshot
    def test_1_Data_Carry_Plus_pack_purchase(self):
        home = Home(self.driver)
        try:
            pass
            home.close_popups()
        except:
            pass
        print("loading app")
        home.wait_visible(home.LOCATOR_HAMBURGER)
        print("loaded")
        del home
        #PurchasePack(self.base).purchase("Data Carry Plus = 415MB [30Days]", 699, '.*',True)
        d = datetime.datetime.now() + datetime.timedelta(days=1)
        SMS=r"Success! You have subscribed to daily JOOX VIP music pack to listen to music in JOOX app.  Enjoy 120MB of JOOX data, valid till \d\d:\d\d:\d\d of {}. Click the link in the other SMS to get JOOX VIP.".format(d.strftime('%d/%m/%Y'))
        PurchasePack(self.base).purchase("120 MB JOOX Data + JOOX VIP [24 hours]", 129, SMS,True)
        sms=Sms(self.base.get_sms_app_driver())
        sms.check_sms(r"Click \{http://www\.joox\.com/mpt\?token=[0-9A-Za-z]{13,19}\} to get JOOX VIP for 24 hours",True)
        sms.check_sms(r"Dear customer, your have received 1 chance to play Hti-Pauk in MPT4U, pls note that this chance would expire in midnight 23:59:59. Click to Play now bit.ly/PlayLuckyDraw and check if you are lucky",True)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_MPT4U)
    unittest.TextTestRunner().run(suite)
