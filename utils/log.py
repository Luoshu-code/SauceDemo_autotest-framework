import logging

def create_logger():
    # 1.创建日志记录器，用于集中管理自动化测试中的日志输出
    logger = logging.getLogger('SauceDemo_logger')
    logger.setLevel(logging.INFO)  # 设置日志级别

    # 配置控制台处理器（StreamHandler），便于开发或测试时即时查看执行状态
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO) # 控制台只显示 INFO 及以上级别
    # 定义日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 将定义好的日志格式（formatter）绑定到处理器（ch）上，确保输出到控制台的日志按指定格式显示
    ch.setFormatter(formatter)

    # 将处理器添加到记录器
    logger.addHandler(ch)
    return logger