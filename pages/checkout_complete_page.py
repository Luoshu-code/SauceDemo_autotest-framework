from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutCompletePage(BasePage):

    Get_order_text_big = (By.CLASS_NAME, "complete-header")
    Get_order_text_min = (By.CLASS_NAME, "complete-text")
    Click_back_home = (By.ID, "back-to-products")

    # thanks 文本
    def get_order_text(self):
        ele1 = self.find_ele(self.Get_order_text_big[0], self.Get_order_text_big[1])
        big_text = ele1.text
        ele2 = self.find_ele(self.Get_order_text_min[0], self.Get_order_text_min[1])
        min_text = ele2.text
        return big_text,min_text
    

    # back home按钮返回商品主页
    def click_back_home(self):
        self.clickable_click(self.Click_back_home[0], self.Click_back_home[1])


    # 购物车重置判断
    def is_cart_reset(self):
        count = self.wdriver.find_elements(By.CLASS_NAME,"shopping_cart_badge")
        if count == []:
            return True
        else:
            return False