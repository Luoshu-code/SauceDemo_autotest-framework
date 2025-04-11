from pages.checkout_one_page import CheckoutOnePage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *
import pytest

# 初始化日志
logger = create_logger()

@allure.feature('Checkout-step one: 取消结账，返回购物车页面')
@allure.story("结账填写信息页面，返回购物车")
@allure.title("Cancel")
def test_checkout_one_cancel(setup_checkout_one):
    
    wdriver = setup_checkout_one
    screenshot_util = Screenshot(wdriver)
    checkout_one_page = CheckoutOnePage(wdriver)

    try: 
        checkout_one_page.click_cancel_checkout_one()
        assert  wdriver.current_url == URL_CART
        logger.info(f"Test Passed: 结账填写信息页面取消，跳转购物车页面成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账填写信息页面取消，跳转购物车页面失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_one_cancel")
        raise 


@allure.feature('Checkout-step one: 结账信息填写完毕，进入Checkout-step two')
@allure.story("结账填写信息结束，进入结账总览页面")
@pytest.mark.parametrize("firstname, lastname, postalcode",[
     ("sang", "zhang" ,"666666"),
     ("", "", "")
 ])
def test_checkout_one_continue(setup_checkout_one,firstname, lastname, postalcode):
    
    allure.dynamic.title(f"firstname:【{firstname}】 lastname:【{lastname}】 postalcode:【{postalcode}】")  # 动态设置标题

    wdriver = setup_checkout_one
    screenshot_util = Screenshot(wdriver)
    checkout_one_page = CheckoutOnePage(wdriver)



    try: 
        checkout_one_page.enter_firstname(firstname)
        checkout_one_page.enter_lastname(lastname)
        checkout_one_page.enter_postalcode(postalcode)
        checkout_one_page.click_continue_checkout_one()
        assert  wdriver.current_url == URL_OVERVIEW
        logger.info(f"Test Passed: 结账信息填写完毕，进入结账总览页面成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账信息填写完毕，进入结账总览页面失败:{e}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_one_continue")
        raise 

# 测试是否输入firstname, lastname, postalcode
@allure.feature('Checkout-step one: 填写结账信息')
@allure.story("测试填写结账信息缺失，能否进入结账下一步")
@pytest.mark.parametrize("firstname, lastname, postalcode",[
    ("sang", "zhang" ,"666666"),
    ("san", "", "666666"),
    ("", "zhang", "666666"),
    ("san", "zhang", ""),
    ("", "", "")
])
def test_checkout_one_enterinfo(setup_checkout_one,firstname, lastname, postalcode):
    
    wdriver = setup_checkout_one
    allure.dynamic.title(f"firstname:【{firstname}】 lastname:【{lastname}】 postalcode:【{postalcode}】")  # 动态设置标题

    screenshot_util = Screenshot(wdriver)
    checkout_one_page = CheckoutOnePage(wdriver)

    try: 
        checkout_one_page.enter_firstname(firstname)
        checkout_one_page.enter_lastname(lastname)
        checkout_one_page.enter_postalcode(postalcode)
        checkout_one_page.click_continue_checkout_one()
        assert  wdriver.current_url == URL_OVERVIEW
        logger.info(f"Test Passed: 结账信息填写测试，进入结账总览页面成功.")

    except Exception as e:
        logger.error(f"Test Failed: 结账信息填写测试，进入结账总览页面失败:{checkout_one_page.not_enter_message()}")  
        screenshot_util.capture_screenshot(test_name="test_checkout_one_enter")
        raise 



    
    





