"""
核心思想：测试对象（页面）和测试用例（页面操作和测试数据）彻底分离

实现方式：
- 一个页面对应一个类，类里面包括元素的定位、操作
- 用例直接去调用页面的操作
"""
import pytest
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from TestDatas import login_datas

# 登录类中每条测试用例都会执行的前后置条件
@pytest.mark.usefixtures("login_init")
class TestLogin():
    # 登录成功
    def test_01_login_success(self,login_init):
        """
        :param login_init: 前置条件返回 driver
        :return:
        """
        LoginPage(login_init).login(*login_datas.success)
        # 断言 登录成功后检查首页是否有"退出"标志
        assert HomePage(login_init).get_element_exists()

    # 步骤：1、登录  2、登录表单区域错误信息断言
    # 使用 @pytest.mark.parametrize("参数名"，数据列表) 进行参数化，不需要解包，替换 ddt
    @pytest.mark.parametrize("test_data",login_datas.cases_from_form_wrong_format)
    def test_02_login_failed_from_form_wrong_format(self,login_init,test_data):
        """
        :param login_init: 前置条件返回 driver
        :param test_data: 登录表单区域测试数据
        :return:
        """
        LoginPage(login_init).login(test_data["username"],test_data["password"])
        # 断言页面登陆表单区域实际的错误提示信息是否等于预期结果
        assert LoginPage(login_init).get_msg_from_login_form() == test_data["expect_result"]

    # 步骤：1、登录  2、登录中间区域错误信息断言
    # 使用 @pytest.mark.parametrize("参数名"，数据列表) 进行参数化，不需要解包，替换 ddt
    @pytest.mark.parametrize("test_data",login_datas.cases_from_middle_wrong_format)
    def test_03_login_failed_from_middle_wrong_format(self,login_init,test_data):
        """
        :param login_init: 前置条件返回 driver
        :param test_data: 登录中间区域测试数据
        :return:
        """
        LoginPage(login_init).login(test_data["username"], test_data["password"])
        # 断言页面登陆中间区域实际的错误提示信息是否等于预期结果
        assert LoginPage(login_init).get_msg_from_login_middle() == test_data["expect_result"]

