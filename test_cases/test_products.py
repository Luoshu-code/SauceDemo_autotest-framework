from pages.products_page import ProductsPage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *
import pytest
from selenium.webdriver.common.by import By


# 初始化日志
logger = create_logger()

# 商品主页加入购物车
@allure.feature('Products: 加入或者移除购物车')
@allure.story("主页：加入购物车")
def test_products_add(setup_addtocart):

    wdriver = setup_addtocart
    products_page = ProductsPage(wdriver)

    screenshot_util = Screenshot(products_page.wdriver) #初始化截图工具

    try:
        products_page.click_AddToCart()
        count = products_page.get_CartCount()

        # 断言：验证是否进入商品页面
        assert count == 6
        logger.info("Test Passed: All products added to cart successfully.")

    except Exception as e:
        logger.error(f"Test Failed: Adding product to cart:{e}")
        screenshot_util.capture_screenshot(test_name="test_add2cart") # 失败时截图
        raise  #重新抛出异常，让pytest标记测试为失败


# 商品主页移除购物车
@allure.feature('Products: 加入或者移除购物车')
@allure.story("主页：移除购物车")
def test_products_remove(setup_remove):
    
    products_page = setup_remove
    screenshot_util = Screenshot(products_page.wdriver) #初始化截图工具

    try:
        products_page.click_remove()
        # 找不到元素不要用封装的显示等待
        assert products_page.wdriver.find_elements(TEST_REMOVE[0], TEST_REMOVE[1]) == [] 
        logger.info("Test Passed: All products removed from cart successfully.")

    except Exception as e:
        logger.error(f"Test Failed: Removing product:{e}")
        screenshot_util.capture_screenshot(test_name="test_remove") # 失败时截图
        raise  #重新抛出异常，让pytest标记测试为失败


# 商品主页排序
@allure.feature('Products: 主页排序')
@allure.story('按姓名AZ排序')
def test_sort_az(setup_sorted):

    wdriver = setup_sorted
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)

    products_page.select_sort(NAME_AZ)

    try:
        res = products_page.is_az_upper()
        assert res == True
        logger.info(f"Test Passed: sort by {NAME_AZ}.")

    except Exception as e:
        logger.error(f"Test Failed: sort by {NAME_AZ}:{e}")  
        screenshot_util.capture_screenshot(test_name="test_sort_by_name_az")
        raise 

# 商品主页排序
@allure.feature('Products: 主页排序')
@allure.story('按姓名ZA排序')
def test_sort_za(setup_sorted):

    wdriver = setup_sorted
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)

    products_page.select_sort(NAME_ZA)

    try:
        res = products_page.is_za_upper()
        assert res == True
        logger.info(f"Test Passed: sort by {NAME_ZA}.")

    except Exception as e:
        logger.error(f"Test Failed: sort by {NAME_ZA}:{e}")  
        screenshot_util.capture_screenshot(test_name="test_sort_by_name_za")
        raise 

@allure.feature('Products: 主页排序')
@allure.story('按价格升序排序')
def test_sort_up(setup_sorted):

    wdriver = setup_sorted
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)

    products_page.select_sort(PRICE_UP)

    try:
        res = products_page.is_low_high()
        assert res == True
        logger.info(f"Test Passed: sort by {PRICE_UP}.")

    except Exception as e:
        logger.error(f"Test Failed: sort by {PRICE_UP}:{e}")  
        screenshot_util.capture_screenshot(test_name="test_sort_by_price_up")
        raise 


@allure.feature('Products: 主页排序')
@allure.story('按价格降序排序')
def test_sort_down(setup_sorted):

    wdriver = setup_sorted
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)

    products_page.select_sort(PRICE_DOWN)

    try:
        res = products_page.is_high_low()
        assert res == True
        logger.info(f"Test Passed: sort by {PRICE_DOWN}.")

    except Exception as e:
        logger.error(f"Test Failed: sort by {PRICE_UP}:{e}")  
        screenshot_util.capture_screenshot(test_name="test_sort_by_price_down")
        raise 

@allure.feature('Products: 主页链接跳转')
@allure.story('图片链接跳转详情')
@pytest.mark.parametrize("product",[
  "Sauce Labs Backpack",
  "Sauce Labs Bike Light",
  "Sauce Labs Bolt T-Shirt",
  "Sauce Labs Fleece Jacket",
  "Sauce Labs Onesie",
  "Test.allTheThings() T-Shirt (Red)"
])
def test_picture_link(setup_link,product):
    
    wdriver = setup_link
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)
    products_page.clickable_click(By.CSS_SELECTOR, f"img[alt='{product}']")
    
    try:
        disc = products_page.find_ele_clickable(By.CSS_SELECTOR, "div[data-test='inventory-item-desc']")
        assert disc.text != None
        logger.info(f"Test Passed: 主页{product}商品图片链接跳转到详情页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 主页{product}商品图片链接跳转到详情页失败:{e}")  
        screenshot_util.capture_screenshot(test_name=f"{product}_test_link_by_picture")
        raise 


@allure.feature('Products: 主页链接跳转')
@allure.story('标题链接跳转详情')
@pytest.mark.parametrize("product",[
  "Sauce Labs Backpack",
  "Sauce Labs Bike Light",
  "Sauce Labs Bolt T-Shirt",
  "Sauce Labs Fleece Jacket",
  "Sauce Labs Onesie",
  "Test.allTheThings() T-Shirt (Red)"
])
def test_title_link(setup_link, product):

    wdriver = setup_link
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)
    products_page.clickable_click(By.XPATH, f"//div[(text()='{product}')]")

    try:
        disc = products_page.find_ele_clickable(By.CSS_SELECTOR, "div[data-test='inventory-item-desc']")
        assert disc.text != None
        logger.info(f"Test Passed: 主页{product}商品标题链接跳转到详情页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 主页{product}商品标题链接跳转到详情页失败:{e}")  
        screenshot_util.capture_screenshot(test_name=f"{product}_test_link_by_title")
        raise 

@allure.feature('Products: 主页跳转到购物车')
@allure.story('跳转到购物车')
def test_cart_link(setup_link):
    wdriver = setup_link
    products_page = ProductsPage(wdriver)
    screenshot_util = Screenshot(products_page.wdriver)
    
    try: 
        products_page.click_cart()
        assert  wdriver.current_url == URL_CART
        logger.info(f"Test Passed: 主页跳转到购物车页面成功.")

    except Exception as e:
        logger.error(f"Test Failed: 主页跳转到购物车页面失败:{e}")  
        screenshot_util.capture_screenshot(test_name=f"test_link_cart")
        raise 













            
        