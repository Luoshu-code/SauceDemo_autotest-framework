# 封装WebDriver的初始化和销毁，支持从配置文件config.yaml(决定使用哪个浏览器)读取浏览器信息

from selenium import webdriver
import yaml   # 配置文件
import logging # 日志模块：提供了一种灵活的方式来记录日志信息

class DriverFactory:
    def __init__(self, config_file = 'config/config.yaml'):
        self.config_file = config_file    # 配置文件

    # 得到配置文件中设置的浏览器种类
    def get_driver(self):
        with open(self.config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)  # 安全地解析 YAML 格式的文件内容，并将其转换为 Python 可操作的数据结构（如字典、列表等）

        browser = config['browser']  # 得到browser设置
        logging.info(f'Launching {browser} browser.') # 记录一条日志信息，表示程序正在启动某个浏览器

        if browser == 'chrome':
            wdriver = webdriver.Chrome()
        elif browser == 'edge':
            wdriver = webdriver.Edge()
        elif browser == 'firefox':
            wdriver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser!")

        return wdriver