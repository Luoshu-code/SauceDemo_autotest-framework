# 本地测试配置文件
# 1.conftest.py文件名不能修改
# 2.conftest.py文件中存放项目所有的fixture，方便对fixture管理和维护
# 3.在conftest.py定义函数
# ①在函数前添加@pytest.fixture()装饰器
# ②在测试用例的函数中传入fixture标识的函数名。
#提示：conftest.py文件放在项目的根目录，作用域是全局的；conftest.py文件放在某一个包下，作用域只在该包内。
from utils.web_base import get_url,reset_app_state
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from cfg import *
import pytest
from selenium.webdriver.support.ui import WebDriverWait # 显示等待
from selenium.webdriver.support import expected_conditions as EC


# 登录功能的初始化
@pytest.fixture(scope='function')
def setup_login():
    # 初始化代码setup
    wdriver = get_url(URL_LOGIN)
    
    yield wdriver # 将wdriver对象传递给测试用例使用

    # 清理代码teardown
    wdriver.quit()


# 商品主页加入购物车功能的初始化
@pytest.fixture(scope='function')
def setup_addtocart():
    # 初始化 - 登录标准用户并进入商品主页
    wdriver = get_url(URL_LOGIN)

    # 登录
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    yield wdriver

    # 后处理：点击清除数据
    reset_app_state(wdriver)

# 商品主页移除购物车功能的初始化
@pytest.fixture(scope='function')
def setup_remove():
    wdriver = get_url(URL_LOGIN)
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    products_page = ProductsPage(wdriver)
    products_page.click_AddToCart()

    yield products_page

    # 后处理：点击清除数据
    reset_app_state(wdriver)


# 商品主页排序功能初始化
@pytest.fixture(scope='function')
def setup_sorted():
    #登录
    wdriver = get_url(URL_LOGIN)
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    yield wdriver

    # 后处理
    wdriver.quit()

# 商品图片链接
@pytest.fixture(scope='function')
def setup_link():
    # 初始化 - 登录标准用户并进入商品主页
    wdriver = get_url(URL_LOGIN)

    # 登录
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    yield wdriver

    # 后处理
    wdriver.quit()

# 购物车页面初始化
@pytest.fixture(scope='function')
def setup_cart():
    # 初始化 - 登录标准用户并进入商品主页
    wdriver = get_url(URL_LOGIN)

    # 登录
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    wdriver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    yield wdriver

    # 后处理
    wdriver.quit()

# checkout_one页面初始化
@pytest.fixture(scope='function')
def setup_checkout_one():

    # 登录
    wdriver = get_url(URL_LOGIN)
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    # 点击购物车
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    wdriver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 点击checkout结账
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "checkout")))
    wdriver.find_element(By.ID, "checkout").click()

    yield wdriver
    
    wdriver.quit()

# checkout_two页面初始化
@pytest.fixture(scope='function')
def setup_checkout_two():

    # 登录
    wdriver = get_url(URL_LOGIN)
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    # 点击购物车
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    wdriver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 在checkout-one页面点击checkout结账
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "checkout")))
    wdriver.find_element(By.ID, "checkout").click()

    # 在checkout-two页面点击continue
    WebDriverWait(wdriver, 10).until(EC.visibility_of_element_located((By.ID, "first-name")))
    wdriver.find_element(By.ID, "first-name").send_keys("san")
    wdriver.find_element(By.ID, "last-name").send_keys("zhang")
    wdriver.find_element(By.ID, "postal-code").send_keys("666666")
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "continue")))
    wdriver.find_element(By.ID, "continue").click()

    yield wdriver
    
    wdriver.quit()

# checkout_comp页面初始化
@pytest.fixture(scope='function')
def setup_checkout_comp():
       # 登录
    wdriver = get_url(URL_LOGIN)
    login_page = LoginPage(wdriver)
    login_page.login(USERNAME, PASSWORD)

    # 加购物车
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    wdriver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 点击购物车
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    wdriver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 在checkout-one页面点击checkout结账
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "checkout")))
    wdriver.find_element(By.ID, "checkout").click()

    # 在checkout-two页面点击continue
    WebDriverWait(wdriver, 10).until(EC.visibility_of_element_located((By.ID, "first-name")))
    wdriver.find_element(By.ID, "first-name").send_keys("san")
    wdriver.find_element(By.ID, "last-name").send_keys("zhang")
    wdriver.find_element(By.ID, "postal-code").send_keys("666666")
    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "continue")))
    wdriver.find_element(By.ID, "continue").click()

    WebDriverWait(wdriver, 10).until(EC.element_to_be_clickable((By.ID, "finish")))
    wdriver.find_element(By.ID, "finish").click()

    yield wdriver

    reset_app_state(wdriver)


