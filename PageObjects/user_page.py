from PageLocators.user_page_locs import UserPageLocs
from Common.basepage import BasePage

class UserPage(BasePage):
    #  个人页面获取用户余额
    def get_user_amount(self):
        return self.get_ele_content(UserPageLocs.user_amount,"个人页面_获取用户余额")
