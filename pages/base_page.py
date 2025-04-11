# BasePage类封装了常用的页面操作
# 例如：查找元素、点击元素、输入文本
# 其他页面对象继承该类，可以减少代码的冗余
### 基类封装所有页面的共同操作，在具体的页面对象中只需调用对应的方法；
### 而在具体的PO对象中：调用基类的方法完成具体的定位元素和操作
### 测试脚本：调用页面类的方法，编写业务逻辑和断言
from selenium.webdriver.support.ui import WebDriverWait # 显示等待
from selenium.webdriver.support import expected_conditions as EC

# 此处只关心对页面对象的操作
class BasePage:
    def __init__(self,wdriver):  # 构造方法
        self.wdriver = wdriver

# 查找元素:创建一个显示等待器，持续检查元素是否存在于 DOM 中
#EC.presence_of_element_located((by, value))检查 DOM 中是否存在符合定位器 (by, value) 的元素。若存在 → 返回该元素的 WebElement 对象；若超时 → 抛出 TimeoutException。
# 返回一个webelement对象
    def find_ele(self, by, value):
        return WebDriverWait(self.wdriver,10).until(EC.presence_of_element_located((by, value)))

    def find_eles(self, by, value):
   # 返回所有匹配的元素列表
        WebDriverWait(self.wdriver, 10).until(EC.visibility_of_element_located((by, value))) 
        return WebDriverWait(self.wdriver, 10).until(EC.presence_of_all_elements_located((by, value)))

# 点击元素
    def click(self, by, value):
        element = self.find_ele(by, value)
        element.click()

# 输入框操作
    def send_keys(self, by, value, text):
        element = self.find_ele(by, value)
        element.send_keys(text)

    # 确保元素可见可交互
    def find_ele_clickable(self, by, value):
        WebDriverWait(self.wdriver, 10).until(EC.element_to_be_clickable((by, value)))
        return WebDriverWait(self.wdriver, 10).until(EC.element_to_be_clickable((by, value)))
    
    def clickable_click(self, by, value):
        WebDriverWait(self.wdriver, 10).until(EC.element_to_be_clickable((by, value)))
        self.click(by, value)