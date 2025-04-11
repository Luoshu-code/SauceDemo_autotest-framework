from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductDetailPage(BasePage):

    get_cartcount = (By.CLASS_NAME,"shopping_cart_badge")
    
    # 点击加入购物车后获取右上角购物车商品的数目
    def get_CartCount(self):
        ele = self.find_ele(self.get_cartcount[0], self.get_cartcount[1])
        return int(ele.text)
     
    # 移除成功判断
    def remove_is_success(self, by , value):
        countremove = self.wdriver.find_elements(by, value)
        if countremove == []:
            return True
        else:
            return False
        
    # 点击返回主页按钮
    def click_backup(self,by, value):
        self.clickable_click(by, value)