import re

import allure
from allure_commons.types import AttachmentType
from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from POM.basepage import basepage


class Sms(basepage):
    LOCATOR_NOLIM = (By.ID, "android:id/button2")
    LOCATOR_DELETE_THREAD = (MobileBy.XPATH, "//*[@text='Delete thread']")
    LOCATOR_MENU = (MobileBy.ACCESSIBILITY_ID, "More options")
    LOCATOR_SELECT = (MobileBy.ACCESSIBILITY_ID, "Select All")
    LOCATOR_DELETE = (MobileBy.ACCESSIBILITY_ID, "Delete")
    LOCATOR_DELETE_CONFIRM = (MobileBy.ID, "android:id/button1")
    LOCATOR_BACK = (MobileBy.ACCESSIBILITY_ID, "Navigate up")

    def __init__(self, driver: Remote):
        self.driver = driver
        #self.driver.start_activity("com.android.mms", 'com.android.mms.ui.ConversationList')

    def close_popup(self):
        self.click(self.LOCATOR_NOLIM)
        return self

    def clear_all_sms(self):
        try:
            self.click(self.LOCATOR_MENU)
            self.click(self.LOCATOR_DELETE_THREAD)
            self.click(self.LOCATOR_SELECT)
            self.click(self.LOCATOR_DELETE)
            self.click(self.LOCATOR_DELETE_CONFIRM)
        except:
            pass

    def check_sms(self, message_text, regex=False, from_text=None):
        xpath = "/hierarchy/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout"
        self.wait_visible((MobileBy.XPATH, xpath + "//android.widget.TextView[1]"))
        if not from_text:
            from_text = ".*"
        print("Checking SMSes")
        i = 0
        while i < len(self.driver.find_elements_by_xpath(xpath)):
            sms_box = self.driver.find_elements_by_xpath(xpath)[i]
            i += 1
            sender = re.sub(r'\s\(\s[0-9]+\s\)$', '',
                            sms_box.find_element_by_xpath("//android.widget.TextView[1]").text)
            if re.match(from_text, sender):
                sms_box.click()
                XPATH = "/hierarchy/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout"
                # check sms text
                self.wait_visible((MobileBy.XPATH, XPATH))
                found_text = False
                for sms_text in self.driver.find_elements_by_xpath(XPATH):
                    print(sms_text.find_element_by_xpath("//android.widget.TextView[1]").text)
                    if regex:
                        if re.match(message_text,
                                    sms_text.find_element_by_xpath("//android.widget.TextView[1]").text):
                            found_text = True
                            allure.attach(self.driver.get_screenshot_as_png(), "SMS_Screenshot", AttachmentType.PNG)
                            break
                        else:
                            if sms_text.find_element_by_xpath("//android.widget.TextView[1]").text == message_text:
                                found_text = True
                                allure.attach(self.driver.get_screenshot_as_png(), "SMS_Screenshot", AttachmentType.PNG)
                                break
                self.click(self.LOCATOR_BACK)
                self.wait_visible((MobileBy.XPATH, xpath + "//android.widget.TextView[1]"))
                if found_text:
                    break
        else:
            for el in self.driver.find_elements_by_xpath("//*"):
                print(el.text)
            assert False, "SMS Not found: " + from_text + "  " + message_text
