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
        hrp = htmlreport.HTMLReport(cls.u, 'report')
        hrp.patch_click()
        cls.u.make_toast("测试开始")
        # cls.u.disable_popups(True)  # 允许自动处理弹出框

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service(
            "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.log=log.log_message()
        self.d = self.u.session("com.esenyun.workline")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass


    def test01BianliContact(self):
        self.log.info_log("遍历通讯录测试开始")
        time.sleep(3)
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(text=u"通讯录(515)").click()
        time.sleep(1)
        self.d(text=u"正式部门").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.d(text=u"认证团队/项目").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.d(text=u"我加入的团队").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.d(text=u"我关注的人").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.log.info_log("遍历通讯录测试结束")

    def test02ChakanKapian(self):
        self.log.info_log("查看卡片测试开始")
        time.sleep(3)
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(text=u"通讯录(515)").click()
        time.sleep(1)
        self.d(text=u"部部全").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/cb_attention").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/cb_attention").click()
        time.sleep(1)
        self.d(text=u"发消息").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/editTextMessage").click()
        time.sleep(1)
        self.d.send_keys("111")
        time.sleep(1)
        self.d(text=u"发送").click()
        time.sleep(1)
        self.log.info_log("查看卡片测试结束")








if __name__ == '__main__':
        unittest.main()
