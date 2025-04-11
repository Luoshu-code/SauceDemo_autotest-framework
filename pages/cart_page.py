from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):

    Click_backup_main = (By.ID, "continue-shopping")
    Click_to_checkout = (By.ID, "checkout")
    Click_cart_remove = (By.CSS_SELECTOR, "button[class='btn btn_secondary btn_small cart_button']")
    Remove_is_success =(By.CLASS_NAME, "cart_item_label")
    Click_cart_products_link =(By.CLASS_NAME, "inventory_item_name")
    Is_cart_to_detail = (By.CLASS_NAME, "inventory_details_desc_container")

    # 从购物车返回到主页
    def click_backup_main(self):
        self.clickable_click(self.Click_backup_main[0], self.Click_backup_main[1])

    # 从购物车跳转到checkout页面
    def click_to_checkout(self):
        self.clickable_click(self.Click_to_checkout[0], self.Click_to_checkout[1])

    # 在购物车点击移除商品
    def click_cart_remove(self):
        self.clickable_click(self.Click_cart_remove[0], self.Click_cart_remove[1])

    # 移除成功判断
    # 此处用find_elements而不用封装的find_eles是因为这里是找不到要显式等待，但此处就是找不到
    def remove_is_success_cart(self):
        countremove = self.wdriver.find_elements(self.Remove_is_success[0], self.Remove_is_success[1])
        if countremove == []:
            return True
        else:
            return False


    # 从购物车点击商品链接
    def click_cart_products_link(self):
        self.clickable_click(self.Click_cart_products_link[0], self.Click_cart_products_link[1])

    # 判断是否从购物车跳转到详情页
    def is_cart_to_detail(self):
        res = self.find_eles(self.Is_cart_to_detail[0], self.Is_cart_to_detail[1])
        if res:
            return True
        else:
            return False