# 截图工具封装：测试用例执行失败时，调用此方法捕获当前页面的截图
# 提供了截图功能，capture-screenshot()方法根据当前测试用例的名称生成截图并保存在指定目录
import os
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Screenshot:

    def __init__(self, wdriver, screenshot_dir="reports/screenshots"):
        self.wdriver = wdriver
        self.screenshot_dir = screenshot_dir
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

    def capture_screenshot(self, test_name):
        # 根据测试用例名称生成截图文件名
        timestamp = time.strftime("%Y%m%d_%H%M%S")   # 生成时间戳
        # 智能路径拼接：e.g. "screenshots\test.png"
        screenshot_path = os.path.join(self.screenshot_dir, f"{test_name}_{timestamp}.png")

        try:
            # 捕获当前页面的截图
            self.wdriver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
           #logging.info(f'Screenshot saved to {screenshot_path}') 
        except Exception as e:
            print(f"Error while taking screenshot:{e}")
           #logging.info(f'Error while taking screenshot:{e}')
        return screenshot_path