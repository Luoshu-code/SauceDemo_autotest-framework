from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.web_base import custom_sort_key


class ProductsPage(BasePage):
    
    Add_to_cart = (By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory ']")
    Remove_cart = (By.CSS_SELECTOR,"button[class='btn btn_secondary btn_small btn_inventory ']")
    After_count_cart = (By.CLASS_NAME,"shopping_cart_badge")
    Select_sort = (By.CLASS_NAME, "product_sort_container")
    Get_all_products_item = (By.CLASS_NAME, "inventory_item_name ")
    Get_all_products_price = (By.CLASS_NAME, "inventory_item_price")
    Picture_link = (By.CLASS_NAME, "inventory_item_img")
    Cart_link = (By.CLASS_NAME, "shopping_cart_link")
    # 点击加入购物车
    def click_AddToCart(self):
        eles = self.find_eles(self.Add_to_cart[0],self.Add_to_cart[1])
        for ele in eles:
            ele.click()

    # 点击加入购物车后获取右上角购物车商品的数目
    def get_CartCount(self):
        ele = self.find_ele(self.After_count_cart[0], self.After_count_cart[1])
        return int(ele.text)
    
    # 主页点击移除购物车
    def click_remove(self):
        eles = self.find_eles(self.Remove_cart[0],self.Remove_cart[1])
        for ele in eles:
            if ele.text == 'Remove':
                ele.click()


    # 得到主页所有商品顺序标题
    def get_all_products_item(self):
        eles = self.find_eles(self.Get_all_products_item[0], self.Get_all_products_item[1])
        list_title = []
        for ele in eles:
            elekey = ele.text
            list_title.append(elekey)
        return list_title

    # 得到主页所有商品顺序价格
    def get_all_products_price(self):
        eles = self.find_eles(self.Get_all_products_price[0], self.Get_all_products_price[1])
        list_price = []
        for ele in eles:
            floatele = float(ele.text.strip('$'))
            list_price.append(floatele)
        return list_price
    
    # 点击排序选择框选择排序方式
    def select_sort(self, sort_method):
        select = Select(self.find_ele(self.Select_sort[0], self.Select_sort[1]))
        select.select_by_visible_text(sort_method)

    # A-Z排序判定
    def is_az_upper(self):
        list_titles = self.get_all_products_item()
        sorted_az_titles = sorted(list_titles, key=custom_sort_key)
        if list_titles == sorted_az_titles:
            return True
        else:
            return False

    # Z-A排序判定
    def is_za_upper(self):
        list_titles = self.get_all_products_item()
        sorted_za_titles = sorted(list_titles, key=custom_sort_key, reverse=True)
        if list_titles == sorted_za_titles:
            return True
        else:
            return False

    # low-high排序判定
    def is_low_high(self):
        list_lohi = self.get_all_products_price()
        if list_lohi == sorted(list_lohi):
            return True
        else:
            return False

    # high-low排序判定
    def is_high_low(self):
        list_hilo = self.get_all_products_price()
        if list_hilo == sorted(list_hilo, reverse=True):
            return True
        else:
            return False

    # # 点击商品图片    
    def click_picture(self, by ,value):
        self.click(by, value)

    # 点击购物车按钮
    def click_cart(self):
        self.clickable_click(self.Cart_link[0], self.Cart_link[1])

