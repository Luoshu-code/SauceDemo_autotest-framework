from pages.product_detail_page import ProductDetailPage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *
import pytest
from selenium.webdriver.common.by import By

# 初始化日志
logger = create_logger()

# 商品详情页加入购物车
@allure.feature('Products Detail: 商品详情页加入或者移除购物车')
@allure.story("详情页：加入购物车")
@pytest.mark.parametrize("product",[
  "Sauce Labs Backpack",
  "Sauce Labs Bike Light",
  "Sauce Labs Bolt T-Shirt",
  "Sauce Labs Fleece Jacket",
  "Sauce Labs Onesie",
  "Test.allTheThings() T-Shirt (Red)"
])
def test_products_add_detail(setup_addtocart, product):

    allure.dynamic.title(f"{product} 详情页加入购物车测试")  # 动态设置标题

    wdriver = setup_addtocart
    # 点击进入商品详情页
    products_page_detail = ProductDetailPage(wdriver)
    screenshot_util = Screenshot(products_page_detail.wdriver)
    products_page_detail.clickable_click(By.XPATH, f"//div[(text()='{product}')]")

    try:
         # 点击加入购物车
        products_page_detail.clickable_click(By.ID, "add-to-cart")
        print("加入购物车成功")
        cartcount = products_page_detail.get_CartCount()
    
        assert cartcount == 1
        logger.info(f"Test Passed: 从{product}的商品详情页加入购物车成功.")

    except Exception as e:
        logger.error(f"Test Failed: 从{product}的商品详情页加入购物车失败:{e}")  
        screenshot_util.capture_screenshot(test_name=f"{product}_detail_add2cart")
        raise 

# 商品详情页移除购物车
@allure.feature('Products Detail: 商品详情页加入或者移除购物车')
@allure.story("详情页：移除购物车")
@pytest.mark.parametrize("product",[
  "Sauce Labs Backpack",
  "Sauce Labs Bike Light",
  "Sauce Labs Bolt T-Shirt",
  "Sauce Labs Fleece Jacket",
  "Sauce Labs Onesie",
  "Test.allTheThings() T-Shirt (Red)"
])
def test_products_remove_detail(setup_addtocart, product):

    allure.dynamic.title(f"{product} 详情页移除购物车测试")  # 动态设置标题

    wdriver = setup_addtocart
    # 点击进入商品详情页
    products_page_detail = ProductDetailPage(wdriver)
    screenshot_util = Screenshot(products_page_detail.wdriver)
    products_page_detail.clickable_click(By.XPATH, f"//div[(text()='{product}')]")

    # 点击加入购物车
    products_page_detail.clickable_click(By.ID, "add-to-cart")
    cartcount = products_page_detail.get_CartCount()
    # 移除前确定购物车加入成功
    if int(cartcount) == 1:
        pass
    try:
        products_page_detail.clickable_click(By.ID, "remove")
        remove_is_success = products_page_detail.remove_is_success(By.CLASS_NAME, "shopping_cart_badge")
        assert remove_is_success == True
        logger.info(f"Test Passed: 从{product}的商品详情页移除购物车成功.")

    except Exception as e:
        logger.error(f"Test Failed: 从{product}的商品详情页移除购物车失败:{e}")  
        screenshot_util.capture_screenshot(test_name=f"{product}_detail_remove_cart")
        raise 

# 商品详情页移除购物车
@allure.feature('Products Detail: 商品详情页返回主页')
@allure.story("详情页：点击返回主页")
@pytest.mark.parametrize("product",[
  "Sauce Labs Backpack",
  "Sauce Labs Bike Light",
  "Sauce Labs Bolt T-Shirt",
  "Sauce Labs Fleece Jacket",
  "Sauce Labs Onesie",
  "Test.allTheThings() T-Shirt (Red)"
])
def test_detail_backup(setup_addtocart, product):

    allure.dynamic.title(f"{product} 详情页返回主页测试")  # 动态设置标题

    wdriver = setup_addtocart
    # 点击进入商品详情页
    products_page_detail = ProductDetailPage(wdriver)
    screenshot_util = Screenshot(products_page_detail.wdriver)
    products_page_detail.clickable_click(By.XPATH, f"//div[(text()='{product}')]")

    try:
        products_page_detail.click_backup(By.ID, "back-to-products")
        assert wdriver.current_url == URL_PRODUCT
        logger.info(f"Test Passed: 从{product}的商品详情页返回主页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 从{product}的商品详情页返回主页失败:{e}")  
        screenshot_util.capture_screenshot(test_name=f"{product}_detail_back_up")
        raise 




