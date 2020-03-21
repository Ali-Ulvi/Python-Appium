
from appium import webdriver

from POM.home import Home
from POM.sms import Sms


class basetest():
    def __init__(self):
        "Setup for the test"
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '5.1'
        self.desired_caps['deviceName'] = 'MPT M50'
        self.desired_caps['udid'] = '710065C12BN0490'
        self.desired_caps['appPackage'] = 'mm.com.mptvas'
        self.desired_caps['appActivity'] = 'com.ztesoft.zsmart.datamall.app.ui.activity.login.LoginWaitingActivity'
        self.desired_caps['skipUnlock'] = True
        self.desired_caps['noReset'] = True
        self.desired_caps['newCommandTimeout'] = 0
        self.get_mpt4u_driver()

    def setup_class(self):
        print("set")

    def click(self, by):
        pass

    def get_mpt4u_driver(self) -> object:
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        home=Home(self.driver)
        home.wait_visible(home.LOCATOR_HAMBURGER)
        return self.driver

    def get_sms_app_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'MPT M50'
        # Returns abs path relative to this file and not cwd
        desired_caps['udid'] = '710065C12BN0490'
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = 'com.android.mms.ui.ConversationList'
        desired_caps['skipUnlock'] = True
        desired_caps['noReset'] = True
        desired_caps['newCommandTimeout'] = 0
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sms=Sms(self.driver)
        sms.wait_visible(sms.LOCATOR_MENU)
        return self.driver
