from pages.checkout_two_page import CheckoutTwoPage
from pages.cart_page import CartPage
from pages.checkout_one_page import CheckoutOnePage
from pages.product_detail_page import ProductDetailPage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *
import pytest
from pages.products_page import ProductsPage
from selenium.webdriver.support.ui import WebDriverWait # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from utils.web_base import is_two_list_equal

# 初始化日志
logger = create_logger()


@allure.feature('Checkout-step two: 取消结账，返回商品主页')
@allure.story("结账总览页面，取消结账返回商品主页")
@allure.title("Cancel")
def test_checkout_two_cancel(setup_checkout_two):

    wdriver = setup_checkout_two
    screenshot_util = Screenshot(wdriver)
    checkout_two_page = CheckoutTwoPage(wdriver)

    try: 
        checkout_two_page.click_cancel_checkout_two()
        assert  wdriver.current_url == URL_PRODUCT
        logger.info(f"Test Passed: 结账总览页面返回商品主页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账总览页面返回商品主页失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_two_cancel")
        raise 


@allure.feature('Checkout-step two: 结账总览完成，点击结束')
@allure.story("结账总览页面确认")
@allure.title("Finsh")
def test_checkout_two_finish(setup_checkout_two):

    wdriver = setup_checkout_two
    screenshot_util = Screenshot(wdriver)
    checkout_two_page = CheckoutTwoPage(wdriver)

    try: 
        checkout_two_page.click_finish_checkout_two()
        assert  wdriver.current_url == URL_FINISH
        logger.info(f"Test Passed: 结账总览页面确认结束成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账总览页面确认结束失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_two_finish")
        raise 

product_groups = [
    ([], 0),
    (["Sauce Labs Backpack"], 1),
    (["Sauce Labs Backpack",  "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"], 3),
    (["Sauce Labs Backpack",  "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"], 6)
] # 商品列表 + 预期数量

@allure.feature('Checkout-step two: 检查商品条目正确性')
@allure.story("测试结账总览页面条目是否与加购的商品相符")
@pytest.mark.parametrize("products, expected_count", product_groups)
def test_check_items_checkout_two(setup_addtocart, products, expected_count):
    
    allure.dynamic.title(f"加入购物车商品数目:{expected_count}")  # 动态设置标题

    # 登录
    wdriver = setup_addtocart
    screenshot_util = Screenshot(wdriver)

    # 加入数据驱动的商品至购物车
    products_page = ProductsPage(wdriver)

    # 主页链接跳转加入购物车
    if int(expected_count) != 0:
        for product in products:
            if product == None:
                pass
            else:
                products_page.clickable_click(By.CSS_SELECTOR, f"img[alt='{product}']")
                products_page.click(By.ID, "add-to-cart")
                products_detail_page = ProductDetailPage(wdriver)
                WebDriverWait(wdriver, 10).until(EC.visibility_of_element_located((By.ID, "back-to-products")))
                ele = products_detail_page.wdriver.find_element(By.ID, "back-to-products")
                ele.click()
    else:
        res = True
    #点击进入购物车页面
    products_page.click_cart()

    # 点击进入checkout页面
    cart_page = CartPage(wdriver)
    cart_page.click_to_checkout()

    # 填写info并点击continue
    checkout_one_page = CheckoutOnePage(wdriver)
    checkout_one_page.enter_firstname("si")
    checkout_one_page.enter_lastname("li")
    checkout_one_page.enter_postalcode("123456")
    checkout_one_page.click_continue_checkout_one()

    checkout_two_page = CheckoutTwoPage(wdriver)
    items = checkout_two_page.get_items_checkout_two()  # 得到总览页面的所有商品标题

# 判断加入的与总览页商品标题是否相同
    res = is_two_list_equal(items, products)
    try: 
        assert res == True
        logger.info(f"Test Passed: 结账总览页面商品条目与加入购物车的一致.")

    except Exception as e:
        logger.error(f"Test Failed: 结账总览页面商品条目与加入购物车的不一致:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_check_items")
        raise 


product_groups = [
    ([], 0),
    (["Sauce Labs Backpack"], 1),
    (["Sauce Labs Backpack",  "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"], 3),
    (["Sauce Labs Backpack",  "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"], 6)
] # 商品列表 + 预期数量

@allure.feature('Checkout-step two: 检查加购商品总价的正确性')
@allure.story("测试结账总览页面商品总价是否为加购商品之和")
@pytest.mark.parametrize("products, expected_count", product_groups)
def test_check_price_checkout_two(setup_addtocart, products, expected_count):
    
    allure.dynamic.title(f"加入购物车商品数目:{expected_count}")  # 动态设置标题

    # 登录
    wdriver = setup_addtocart
    screenshot_util = Screenshot(wdriver)

    # 加入数据驱动的商品至购物车
    products_page = ProductsPage(wdriver)

    # 主页链接跳转加入购物车
    if int(expected_count) != 0:
        for product in products:
            if product == None:
                pass
            else:
                products_page.clickable_click(By.CSS_SELECTOR, f"img[alt='{product}']")
                products_page.click(By.ID, "add-to-cart")
                products_detail_page = ProductDetailPage(wdriver)
                WebDriverWait(wdriver, 10).until(EC.visibility_of_element_located((By.ID, "back-to-products")))
                ele = products_detail_page.wdriver.find_element(By.ID, "back-to-products")
                ele.click()

    #点击进入购物车页面
    products_page.click_cart()

    # 点击进入checkout页面
    cart_page = CartPage(wdriver)
    cart_page.click_to_checkout()

    # 填写info并点击continue
    checkout_one_page = CheckoutOnePage(wdriver)
    checkout_one_page.enter_firstname("si")
    checkout_one_page.enter_lastname("li")
    checkout_one_page.enter_postalcode("123456")
    checkout_one_page.click_continue_checkout_one()

    checkout_two_page = CheckoutTwoPage(wdriver)
    totalprices_add = checkout_two_page.get_add_totalprice() # 得到总览页面的所有商品标题
    
    totalprice = checkout_two_page.get_totalprice()

    try: 
        assert totalprices_add == totalprice
        logger.info(f"Test Passed: 结账总览页面商品总价与加入购物车商品单价之和相同.")

    except Exception as e:
        logger.error(f"Test Failed: 结账总览页面商品总价与加入购物车商品单价之和不相同:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_check_totalprice")
        raise 




    

  









