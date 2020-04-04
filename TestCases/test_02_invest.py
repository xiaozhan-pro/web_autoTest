"""
在前置条件中登录
1、进入首页选择第一个标
2、进入标页面
    -获取投资前用户余额
    -获取投资前标余额
    -输入2000，点击"投标"
3、在标页面弹出"投标成功"提示，并点击"查看并激活"
4、进入个人页面，获取账户余额
5、返回到标页面并刷新页面
6、获取标可投金额
"""
import pytest
from PageObjects.bid_page import BidPage
from PageObjects.home_page import HomePage
from PageObjects.user_page import UserPage
from decimal import Decimal

# 登录类中每条测试用例都会执行的前后置条件
@pytest.mark.usefixtures("invest_init")
class TestInvest():
    def test_01_invest_success(self,invest_init):
        """
        :param invest_init: 前置条件返回 driver
        :return:
        """
        #  进入首页选择第一个标
        HomePage(invest_init).choice_first_bid()

        #获取投资前用户余额
        get_user_before_amount = BidPage(invest_init).get_user_amount()

        # 获取投资前标余额
        get_bid_before_amount = BidPage(invest_init).get_bid_amount()

        #输入100，点击"投标"
        BidPage(invest_init).invest(100)

        # 在标页面弹出"投标成功"提示，并点击"查看并激活"
        BidPage(invest_init).click_active_button_in_success_popup()

        # 进入个人页面，获取投资后用户余额
        get_user_after_amount = UserPage(invest_init).get_user_amount().strip("元")  #删去中文"元"

        # 投资前后用户余额的差值
        user_diff_money = Decimal(get_user_before_amount) - Decimal(get_user_after_amount)
        # 断言投资前后用户余额的差值是否和预期结果相等
        assert user_diff_money == Decimal(str(100))

        # 返回到标页面并刷新页面,获取投资后标可投金额
        invest_init.back()
        invest_init.refresh()
        get_bid_after_amount = BidPage(invest_init).get_bid_amount()

        # 投资前后标余额的差值
        bid_diff_money = Decimal(get_bid_before_amount)- Decimal(get_bid_after_amount)
        # 断言投资前后标余额的差值是否和预期结果相等
        # 例如8.01万-8万=0.01,则需要乘以10000
        if bid_diff_money < Decimal(str(1)):
            assert Decimal(str(100)) == bid_diff_money * 10000
        # 例如8000-7900=100,直接断言即可
        else:
            assert Decimal(str(100)) == bid_diff_money
