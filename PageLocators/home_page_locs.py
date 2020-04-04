"""
独立测试数据：
- 方便修改
- 方便共享
- 方便环境切换/多环境共用
"""

from selenium.webdriver.common.by import By
# 主页元素定位
class HomePageLocs():
    # 退出
    quit_login = (By.XPATH,'//a[text()="退出"]')
    # 第一个标
    first_bid = (By.XPATH,'//a[@class="btn btn-special"]')
