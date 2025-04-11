from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutTwoPage(BasePage):

    Click_cancel_checkout_two = (By.ID, "cancel")
    Click_finish_checkout_two = (By.ID, "finish")
    Get_items_checkout_two = (By.CSS_SELECTOR, "[class='inventory_item_name']")
    Get_add_totalprice = (By.CSS_SELECTOR, "[class='inventory_item_price']")
    Get_totalprice = (By.CSS_SELECTOR, "[class='summary_subtotal_label']")

    # 点击取消按钮，返回商品主页
    def click_cancel_checkout_two(self):
        self.clickable_click(self.Click_cancel_checkout_two[0], self.Click_cancel_checkout_two[1])


    # 点击finish按钮，完成结账
    def click_finish_checkout_two(self):
        self.clickable_click(self.Click_finish_checkout_two[0], self.Click_finish_checkout_two[1])


    # Overview商品条目信息正确测试
    def get_items_checkout_two(self):
        eles = self.wdriver.find_elements(self.Get_items_checkout_two[0], self.Get_items_checkout_two[1])
        if eles == []:
            return []
        else:
            titles = []
            for ele in eles:
                title = ele.text
                titles.append(title)
            return titles
        

    # 页面商品单价加和得到total price
    def get_add_totalprice(self):
        eles = self.wdriver.find_elements(self.Get_add_totalprice[0], self.Get_add_totalprice[1])
        totalprice = 0
        for ele in eles:
            newprice = ele.text
            price = float(newprice[1:])
            totalprice += price
        return totalprice
    
    # 
    def get_totalprice(self):
        ele = self.find_ele(self.Get_totalprice[0], self.Get_totalprice[1])
        fulltext = ele.text
        # 用 "$" 分割后取第二部分，再去除空格
        totalprice = float(fulltext.split("$")[-1].strip())
        return totalprice

    

        
  