from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutOnePage(BasePage):
    
    Click_cancel_checkout_one = (By.ID, "cancel")
    Click_continue_checkout_one = (By.ID, "continue")
    Enter_firstname = (By.ID , "first-name")
    Enter_lastname = (By.ID , "last-name")
    Enter_postalcode = (By.ID , "postal-code")
    Not_enter_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 点击取消按钮，返回购物车
    def click_cancel_checkout_one(self):
        self.clickable_click(self.Click_cancel_checkout_one[0], self.Click_cancel_checkout_one[1])

    # 点击继续按钮，进入结账第二部
    def click_continue_checkout_one(self):
        self.clickable_click(self.Click_continue_checkout_one[0], self.Click_continue_checkout_one[1])

    # 在输入框中填写First Name内容
    def enter_firstname(self, firstname):
        self.send_keys(self.Enter_firstname[0], self.Enter_firstname[1], firstname)

    # 在输入框中填写Last Name内容
    def enter_lastname(self, lastname):
        self.send_keys(self.Enter_lastname[0], self.Enter_lastname[1], lastname)

    # 在输入框中填写Postal code内容
    def enter_postalcode(self, postalcode):
        self.send_keys(self.Enter_postalcode[0], self.Enter_postalcode[1], postalcode)

    # 未填入First Name\Last Name\Postal code，弹窗消息获取
    def not_enter_message(self):
        ele = self.find_ele(self.Not_enter_message[0], self.Not_enter_message[1])
        return ele.text