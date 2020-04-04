from selenium.webdriver.common.by import By
# 标页元素定位
class BidPageLocs():
    # 用户投资额输入框
    user_amount = (By.XPATH,'//input[@data-url="/Invest/invest"]')
    # 标余额
    bid_amount = (By.XPATH,'//span[@class="mo_span4"]')
    # 投标
    invest = (By.XPATH,'//button[@class="btn btn-special height_style"]')
    # "查看并激活"按钮
    click_active_button = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')