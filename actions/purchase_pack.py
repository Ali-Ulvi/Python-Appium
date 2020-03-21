import allure

from POM.home import Home
from POM.sms import Sms


class PurchasePack:
    def __init__(self, basetest):
        self.driver = basetest.driver
        self.base=basetest

    def purchase(self, pack_name, price, sms_text=None,regex=False,sms_sender=None ):
        if sms_text :
            sms = Sms(self.base.get_sms_app_driver())
            sms.clear_all_sms()
            self.driver=self.base.get_mpt4u_driver()
        home = Home(self.driver)
        home.save_money()
        home.clickPackPurchase().clickPurchaseButtonFor(pack_name).assertOfferName(
            pack_name).purchase().yes().assertSuccessText()
        home.check_price(price)
        if sms_text :
            sms = Sms(self.base.get_sms_app_driver())
            sms.check_sms(sms_text,regex, sms_sender)

            self.driver=self.base.get_mpt4u_driver()
