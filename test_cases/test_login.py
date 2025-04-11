import pytest
from pages.login_page import LoginPage
from utils.log import create_logger
from utils.screenshot import Screenshot
import allure
from cfg import *

# 初始化日志
logger = create_logger()

# 登录功能的数据驱动
@allure.feature('Login')
@pytest.mark.parametrize("username, password",[
("standard_user","secret_sauce"), 
("locked_out_user","secret_sauce"),
("problem_user","secret_sauce"),
("performance_glitch_user","secret_sauce"),
("error_user","secret_sauce"),
("visual_user","secret_sauce")
])
def test_login(setup_login, username, password):

    allure.dynamic.story(f"{username}用户登录")  # 根据 username 动态设置 Story
    allure.dynamic.title(f"{username} 用户登录")  # 动态设置标题

    wdriver = setup_login    # 接收fixture返回的wdriver对象
    screenshot_util = Screenshot(wdriver) #初始化截图工具
    login_page = LoginPage(wdriver) 

    try:
        login_page.login(username, password)

        # 断言：验证是否进入商品页面
        assert wdriver.current_url == URL_PRODUCT
        logger.info("Login test passed")

    except Exception as e:
        logger.error(f"Login test failed:{e}")
        screenshot_util.capture_screenshot(test_name="test_login") # 失败时截图
        raise  #重新抛出异常，让pytest标记测试为失败
