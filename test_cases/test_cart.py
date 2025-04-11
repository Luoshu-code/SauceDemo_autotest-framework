from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *
import pytest
from selenium.webdriver.common.by import By

# 初始化日志
logger = create_logger()

@allure.feature('Cart: 购物车返回主页')
@allure.story("购物车详情页返回主页，继续购物")
def test_backup_main(setup_cart):
    
    wdriver = setup_cart

    screenshot_util = Screenshot(wdriver)
    cart_page = CartPage(wdriver)

    try: 
        cart_page.click_backup_main()
        assert  wdriver.current_url == URL_PRODUCT
        logger.info(f"Test Passed: 购物车页面跳转到主页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 购物车页面跳转到主页失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_link_cart_backup_main")
        raise 

@allure.feature('Cart: 购物车跳转到checkout')
@allure.story("购物车详情页跳转到checkout")
def test_checkout(setup_cart):

    wdriver = setup_cart

    screenshot_util = Screenshot(wdriver)
    cart_page = CartPage(wdriver)

    try: 
        cart_page.click_to_checkout()
        assert  wdriver.current_url == URL_CHECKOUT
        logger.info(f"Test Passed: 购物车跳转到checkout页面成功.")

    except Exception as e:
        logger.error(f"Test Failed: 购物车跳转到checkout页面失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_link_cart_checkout")
        raise 

# 移除购物车中的商品
@allure.feature('Cart: 移除购物车中的商品')
@allure.story("移除购物车中的商品")
@pytest.mark.parametrize("product",[
  "add-to-cart-sauce-labs-backpack",
  "add-to-cart-sauce-labs-bike-light",
  "add-to-cart-sauce-labs-bolt-t-shirt",
  "add-to-cart-sauce-labs-fleece-jacket",
  "add-to-cart-sauce-labs-onesie",
  "add-to-cart-test.allthethings()-t-shirt-(red)"
])
def test_cart_remove(setup_addtocart, product):

    new_product = product[12:]
    allure.dynamic.title(f"移除购物车中的{new_product}测试")  # 动态设置标题

    wdriver = setup_addtocart
    products_page = ProductsPage(wdriver)

    screenshot_util = Screenshot(products_page.wdriver) #初始化截图工具
    
    # 把商品加入购物车
    products_page.clickable_click(By.ID, f"{product}")
    count = products_page.get_CartCount()
    if count == 1:
        products_page.click_cart()

    cart_page = CartPage(wdriver)

    try: 
        cart_page.click_cart_remove()
        res = cart_page.remove_is_success_cart()
        assert res
        logger.info(f"Test Passed: 购物车移除{new_product}成功.")

    except Exception as e:
        logger.error(f"Test Failed: 购物车移除{new_product}失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_cart_remove")
        raise 


# 点击购物车中的商品链接跳转到详情页
@allure.feature('Cart: 跳转到购物车中的商品详情页')
@allure.story("从购物车跳转到商品的详情页")
@pytest.mark.parametrize("product",[
  "add-to-cart-sauce-labs-backpack",
  "add-to-cart-sauce-labs-bike-light",
  "add-to-cart-sauce-labs-bolt-t-shirt",
  "add-to-cart-sauce-labs-fleece-jacket",
  "add-to-cart-sauce-labs-onesie",
  "add-to-cart-test.allthethings()-t-shirt-(red)"
])
def test_cart_link_detail(setup_addtocart, product):

    new_product = product[12:]
    allure.dynamic.title(f"购物车中的{new_product}跳转到商品详情页测试")  # 动态设置标题


    wdriver = setup_addtocart
    products_page = ProductsPage(wdriver)

    screenshot_util = Screenshot(products_page.wdriver) #初始化截图工具
    
    # 把商品加入购物车
    products_page.clickable_click(By.ID, f"{product}")
    count = products_page.get_CartCount()
    if count == 1:
        products_page.click_cart()

    cart_page = CartPage(wdriver)

    try: 
        cart_page.click_cart_products_link()
        res = cart_page.is_cart_to_detail()
        assert res
        logger.info(f"Test Passed: 购物车的{new_product}跳转到详情页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 购物车的{new_product}跳转到详情页失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_cart_link_detail")
        raise 










    