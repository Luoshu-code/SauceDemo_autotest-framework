# LoginPage继承BasePage类
# PO页面对象模式：将每个页面抽象为一个类，封装页面元素和操作逻辑
# 优点：提升代码的可维护性、复用性和可读性
#1.高内聚低耦合：元素定位和操作逻辑集中在页面类中，测试脚本仅调用方法。
#2.复用性增强：同一页面的操作可被多个测试用例复用。
#3.易于维护：页面结构变化时，仅需修改对应的页面类。
from selenium.webdriver.common.by import By
from .base_page import BasePage


# 封装登录页面的元素定位和操作
class LoginPage(BasePage):
    username_input = (By.ID, 'user-name')
    pwd_input = (By.ID, 'password')
    login_button  = (By.ID, 'login-button')

    def enter_username(self, username):
        self.send_keys(self.username_input[0], self.username_input[1], username)

    def enter_pwd(self, pwd):
        self.send_keys(self.pwd_input[0], self.pwd_input[1], pwd)

    def click_login(self):
        self.click(self.login_button[0], self.login_button[1])

    # 封装登录
    def login(self, user ,pwd):
        self.enter_username(user)
        self.enter_pwd(pwd)
        self.click_login()

