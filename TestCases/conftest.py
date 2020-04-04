import pytest
from selenium import webdriver
from TestDatas import Global_Datas
from PageObjects.login_page import LoginPage

# 定义一个登录的前后置函数
@pytest.fixture(scope="function")
def login_init():
    # 打开会话
    # 每次重新打开一个会话是为了保证用例的独立性，因为不知道在哪个页面会失败，没法保证接下来的用例能够执行
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 打开前程贷官网
    driver.get(Global_Datas.login_url)

    # yield生成器--前后置分离，返回driver
    yield driver

    # 关闭会话
    driver.quit()

# 定义一个投资的前后置函数
@pytest.fixture(scope="function")
# 调用 login_init 的前后置，并且将 login_init 的返回值作为参数传入
def invest_init(login_init):
    LoginPage(login_init).login(*Global_Datas.user_invest)

    # 前后置分离，返回driver
    yield login_init

    # 关闭会话
    login_init.quit()