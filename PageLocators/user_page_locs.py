from selenium.webdriver.common.by import By
# 个人页元素定位
class UserPageLocs():
    # 可用余额
    user_amount = (By.XPATH,'//li[@class="color_sub"]')