from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageLocators.login_page_locs import LoginPageLocs
from Common.basepage import BasePage

class LoginPage(BasePage):
    # 登录成功
    def login(self,username,password):
        # 输入手机号
        self.input_text(LoginPageLocs.user_input,"登录页面_输入手机号",username)
        # 输入密码
        self.input_text(LoginPageLocs.password_input,"登录页面_密码",password)
        # 登录
        self.click_element(LoginPageLocs.login_button,"登录页面_登录")

    # 从登录表单区域获取错误信息
    def get_msg_from_login_form(self):
        # 等待"登录表单区域的提示信息"的出现
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LoginPageLocs.msg_from_login_form))

        # 如果有1个错误信息，直接返回错误文本内容
        # 如果多个错误信息，可存与列表中方便调用
        eles = self.driver.find_elements(*LoginPageLocs.msg_from_login_form)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            text_list = []
            for ele in eles:
                text_list.append(ele)
            return text_list

    # 从登录页面中间区域获取错误信息
    def get_msg_from_login_middle(self):
        # 等待"登录表单区域的提示信息"的出现
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LoginPageLocs.msg_from_login_middle))

        # 如果有1个错误信息，直接返回错误文本内容
        # 如果多个错误信息，可存与列表中方便调用
        eles = self.driver.find_elements(*LoginPageLocs.msg_from_login_middle)
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            text_list = []
            for ele in eles:
                text_list.append(ele)
            return text_list









