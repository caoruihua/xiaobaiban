#-*-coding:utf-8-*- 
__author__ = 'Administrator'

# coding: utf-8
import unittest
import uiautomator2 as u2
import time
from public import cofig


class TestXiaobaiban(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect(cofig.ID)
        cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        #hrp = htmlreport.HTMLReport(cls.u, 'report')
        #hrp.patch_click()
        cls.u.make_toast("测试开始")
        # cls.u.disable_popups(True)  # 允许自动处理弹出框

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service(
            "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.d = self.u.session("com.esenyun.workline.dev")  # restart app


        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass


    def test01TuanduiKanban(self):
        self.d(text=u"感谢信").click()
        time.sleep(4)
        driver = ChromeDriver(self.u).driver(cofig.ip2)
        print("webview测试开始")
        driver.find_element_by_xpath('/html/body/ion-app/ng-component/ion-nav/page-setting-center/ion-content/div[2]/ion-list[2]/div[1]').click()
        print('已点击')
        time.sleep(3)
        self.d.press("back")
        time.sleep(3)





if __name__ == '__main__':
        unittest.main()