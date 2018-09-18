# coding: utf-8
import unittest
import uiautomator2 as u2
import time
from public import log,cofig
import uiautomator2.ext.htmlreport as htmlreport
import logging


class TestXiaobaiban(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb(cofig.ID)
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
        self.d = self.u.session("com.esenyun.workline")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass



    def test01Qiehuanzuzhi(self):
        u'''测试切换租户'''
        time.sleep(3)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right01").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/trm_menu_item_text", text=u"切换组织").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_company_name", text=u"小森网络").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
if __name__ == '__main__':
        unittest.main()
