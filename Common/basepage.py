"""
日志：记录用例执行的过程
截图：报错时进行截图，方便定位问题
BasePage
- webdriver-API二次封装
- 每个页面操作都会进行失败截图，操作信息/错误信息写入到日志中，方便定位问题
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

from Common import dir_config
from Common.Logger_handler import LoggerHandler
import os

# 初始化日志处理器
logger = LoggerHandler()

class BasePage():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 等待可见
    def wait_ele_visible(self,loc,img_name,timeout=20,poll_fre=0.5):
        # 等待开始时，记录当前时间
        before_ts = datetime.now()
        logger.info("在'{}'页面等待{}元素可见".format(img_name, loc))
        try:
            WebDriverWait(self.driver,timeout,poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except TimeoutException as e :
            # 等待超时截图，写入详细报错信息到日志中
            self.save_page_shot(img_name)
            logger.exception("等待超时!错误信息如下")
            # 抛出异常
            raise e

    # 查找元素
    def get_element(self,loc,img_name,timeout=20,poll_fre=0.5):
        logger.info("在'{}'页面中查找元素：{}".format(img_name, loc))
        try:
            return self.driver.find_element(*loc)
        except:
            # 失败截图，写入详细报错信息到日志中
            self.save_page_shot(img_name)
            logger.exception("查找元素失败!错误信息如下")
            # 抛出异常
            raise

    # 点击
    def click_element(self,loc,img_name,timeout=20,poll_fre=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        # 查找元素
        ele = self.get_element(loc, img_name, timeout, poll_fre)
        logger.info("在'{}'页面中点击{}元素".format(img_name, loc))
        try:
            # 点击元素
            ele.click()
        except:
            # 失败截图，写入详细报错信息到日志中
            self.save_page_shot(img_name)
            logger.exception("点击元素失败!错误信息如下")
            # 抛出异常
            raise

    # 输入文本
    def input_text(self,loc,img_name,text,timeout=20,poll_fre=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        # 查找元素
        ele = self.get_element(loc, img_name, timeout, poll_fre)
        logger.info("在'{}'页面中向{}输入'{}'".format(img_name, loc, text))
        try:
            # 输入文本
            ele.send_keys(text)
        except:
            # 失败截图，写入详细报错信息到日志中
            self.save_page_shot(img_name)
            logger.exception("输入文本失败!错误信息如下")
            # 抛出异常
            raise

    # 获取元素文本内容
    def get_ele_content(self,loc,img_name,timeout=20,poll_fre=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        # 查找元素
        ele = self.get_element(loc, img_name, timeout, poll_fre)
        logger.info("在'{}'页面中获取{}元素文本内容".format(img_name, loc))
        try:
            # 获取元素属性
            text =  ele.text
            logger.info("获取的文本是：{}".format(text))
            return text

        except:
            # 失败截图，写入详细报错信息到日志中
            self.save_page_shot(img_name)
            logger.exception("获取文本失败!错误信息如下")
            # 抛出异常
            raise

    # 获取元素属性的值
    def get_ele_attribute(self,loc,img_name,className,timeout=20,poll_fre=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        # 查找元素
        ele = self.get_element(loc, img_name, timeout, poll_fre)
        logger.info("在'{}'页面中获取{}元素的属性".format(img_name, loc))
        try:
            # 获取元素属性
            attr = ele.get_attribute(className)
            logger.info("获取的属性是：{}".format(attr))
            return ele.get_attribute(className)
        except:
            # 失败截图，写入详细报错信息到日志中
            self.save_page_shot(img_name)
            logger.exception("获取属性失败!错误信息如下")
            # 抛出异常
            raise

    # iframe切换
    def switch_to_iframe(self,loc):
        try:
            # 等待iframe可见并且切换进去
            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            pass

    # 失败截图，写入日志
    def save_page_shot(self,img_name):
        """
        :param img_name:{页面名称，页面行为}
        :return:
        将图片存储到Outputs的screenshots下，唯一不同是图片的命名
        命名规范：{页面名称_页面行为}_时间.png
        """
        # 获取当前时间
        ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # 创建文件路径
        file_name = "{}_{}.png".format(img_name,ts)
        file_path = os.path.join(dir_config.screenshots_path,file_name)
        # 保存截图到相应路径下
        self.driver.save_screenshot(file_path)
        logger.info("已截取当前页面保存在:{}".format(file_path))

if __name__=="__main__":
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    bp = BasePage(driver)
    loc_input = (By.XPATH,'//input[@id="kw"]')
    loc_search = (By.XPATH,'//input[@id="su"]')
    loc_content = (By.XPATH,'//a[@sync="true"]')
    loc_attribute =(By.XPATH,'//span[text()="相关软件"]')
    bp.input_text(loc_input,"百度首页_搜索输入框","selenium webdriver")
    logger.info("*******************")
    bp.click_element(loc_search,"百度首页_点击搜索")
    logger.info("*******************")
    bp.get_ele_content(loc_content,"百度首页_获取文本")
    logger.info("*******************")
    bp.get_ele_attribute(loc_attribute,"百度首页_获取属性","title")
    driver.close()
    driver.quit()


