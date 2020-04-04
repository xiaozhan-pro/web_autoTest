from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageLocators.bid_page_locs import BidPageLocs
from Common.basepage import BasePage

class BidPage(BasePage):
    #获取账户余额
    def get_user_amount(self):
        return  self.get_ele_attribute(BidPageLocs.user_amount,"标页面_获取账户余额","data-amount")

    #获取标可投金额
    def get_bid_amount(self):
        return  self.get_ele_content(BidPageLocs.bid_amount,"标页面_获取标可投金额")

    # 输入100元，点击'投标'
    def invest(self,money):
        self.input_text(BidPageLocs.user_amount,"标页面_输入100元",money)
        self.click_element(BidPageLocs.invest,"标页面_点击'投标'")

    # 在'投标成功'提示中点击'查看并激活'
    def click_active_button_in_success_popup(self):
        self.click_element(BidPageLocs.click_active_button,"标页面_在'投标成功'提示中点击'查看并激活'")



