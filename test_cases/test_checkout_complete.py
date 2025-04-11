from pages.checkout_complete_page import CheckoutCompletePage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *
import pytest



# 初始化日志
logger = create_logger()


@allure.feature('Checkout-complete: 结账完毕')
@allure.story("结账完毕页面，显示感谢购物文本")
@allure.title("Order")
def test_checkout_comp_text(setup_checkout_comp):
    
    wdriver = setup_checkout_comp
    screenshot_util = Screenshot(wdriver)
    checkout_complete_page = CheckoutCompletePage(wdriver)
    bigtext,mintext = checkout_complete_page.get_order_text()

    try: 
        assert  (bigtext == BIGTEXT) and (mintext == MINTEXT)
        logger.info(f"Test Passed: 结账总览页面文本显示成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账总览页面文本显示失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_comp_text")
        raise     

@allure.feature('Checkout-complete: 返回主页')
@allure.story("结账完毕页面，点击返回主页")
@allure.title("Back Home")
def test_checkout_comp_backhome(setup_checkout_comp):
    
    wdriver = setup_checkout_comp
    screenshot_util = Screenshot(wdriver)
    checkout_complete_page = CheckoutCompletePage(wdriver)
    checkout_complete_page.click_back_home()

    try: 
        assert wdriver.current_url == URL_PRODUCT
        logger.info(f"Test Passed: 结账返回主页成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账返回主页失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_comp_backhome")
        raise 

@allure.feature('Checkout-complete: 购物车重置')
@allure.story("结账完毕，测试购物车是否重置")
@allure.title("cart reset")
def test_is_cart_reset(setup_checkout_comp):

    wdriver = setup_checkout_comp
    screenshot_util = Screenshot(wdriver)
    checkout_complete_page = CheckoutCompletePage(wdriver)
    res = checkout_complete_page.is_cart_reset()

    try: 
        assert res == True
        logger.info(f"Test Passed: 结账后购物车重置成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账后购物车重置失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_comp_cartreset")
        raise 




    

 