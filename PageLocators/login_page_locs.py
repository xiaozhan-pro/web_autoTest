"""
独立测试数据：
- 方便修改
- 方便共享
- 方便环境切换/多环境共用
"""

from selenium.webdriver.common.by import By

# 登录页面元素定位
class LoginPageLocs():
    # 用户名输入框
    user_input = (By.XPATH,'//input[@name="phone"]')
    # 密码输入框
    password_input = (By.XPATH,'//input[@name="password"]')
    # "登录"按钮
    login_button = (By.XPATH,'//button[text()="登录"]')
    #  登录表单区域的提示信息框
    msg_from_login_form = (By.XPATH,'//div[@class="form-error-info"]')
    #  页面中间区域的提示信息框
    msg_from_login_middle = (By.XPATH,'//div[@class="layui-layer-content"]')



