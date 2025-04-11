from utils.driver_factory import DriverFactory
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait # 显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from collections import Counter
# 封装常用的功能函数

    
# 打开网站
def get_url(url):
    driver_factory = DriverFactory()
    wdriver = driver_factory.get_driver() # 返回一个wd对象
    wdriver.get(url)
    return wdriver

# 重置网站状态
def reset_app_state(wdriver):
    wdriver.find_element(By.ID, "react-burger-menu-btn").click()
    # 创建 actions 的 ActionChains 对象
    actions = ActionChains(wdriver)
    # 定位到需要点击的按钮
    click = wdriver.find_element(By.ID, "reset_sidebar_link")
    # 等待元素可见
    element = WebDriverWait(wdriver, 10).until(EC.visibility_of_element_located((By.ID, "reset_sidebar_link")))
    # 元素不在可视区域内:使用 JavaScript 滚动到元素
    wdriver.execute_script("arguments[0].scrollIntoView(true);", click)
    # 将鼠标移动到按钮上
    actions.move_to_element(click)
    # 鼠标左键
    actions.click()
    # 执行操作(必须要有该方法,否则操作不会执行)
    actions.perform()
    wdriver.quit()

    # 标题预处理：移除非字母字符，仅保留A-Za-z，然后转为小写
def custom_sort_key(s):
    return re.sub('[^A-Za-z]', '', s).lower()

# 判定两个列表内容是否相同（顺序可不一致）
def is_two_list_equal(list1, list2):
    if Counter(list1) == Counter(list2):
        return True
    else:
        return False