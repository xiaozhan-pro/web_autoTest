from PageLocators.home_page_locs import HomePageLocs
from Common.basepage import BasePage

class HomePage(BasePage):
    # 登录成功后检查首页是否有'退出'标志
    def get_element_exists(self):
        try:
            self.wait_ele_visible(HomePageLocs.quit_login,"主页_登录成功后检查首页是否有'退出'标志")
            return True
        except:
            return False

    # 选择第一个标
    def choice_first_bid(self):
        self.click_element(HomePageLocs.first_bid,"主页_选择第一个标")
