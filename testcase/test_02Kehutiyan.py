# coding: utf-8
import unittest
import uiautomator2 as u2
import time
from public import log,cofig
import uiautomator2.ext.htmlreport as htmlreport
from public import log


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
        self.log = log.log_message()
        self.d = self.u.session("com.esenyun.workline")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass



    def test01Jibenbianli(self):  # 进入客户体验进行菜单遍历
        self.log.info_log("开始遍历客户体验菜单")
        time.sleep(1)
        self.d(text="客户体验").click()
        time.sleep(3)
        self.d(resourceId="com.esenyun.workline:id/iv_title_right").click()  # 进入dashboard
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/iv_title_left").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_title_right02").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/trm_menu_item_text").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_title_left").click()
        time.sleep(1)
        self.d.swipe(0.968, 0.516, 0.051, 0.516)
        time.sleep(2)
        self.d.click(0.593, 0.418)
        time.sleep(1)
        self.d.click(0.784, 0.968)
        self.log.info_log("客户体验菜单遍历结束")
        time.sleep(2)

if __name__ == '__main__':
        unittest.main()
