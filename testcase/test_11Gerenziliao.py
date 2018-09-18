# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport
import logging


class TestXiaobaiban(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
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



    def test01Chakanjuese(self): #查看角色
        u'''查看角色'''
        self.d(text=u"我的").click()
        time.sleep(3)
        self.d(text=u"待完善").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_roles_more").click()
        time.sleep(3)

    def test02Canyudu(self):
        u'''查看参与度'''
        self.d(text=u"我的").click()
        time.sleep(3)
        self.d(text=u"我的参与度").click()
        time.sleep(2)
        self.d.swipe(0.474, 0.944,0.482, 0.263)
        time.sleep(1)
        self.d.swipe(0.482, 0.263,0.474, 0.944, )
        time.sleep(2)
        self.d.click(0.912, 0.163) #进入历史参与度

    def test03Weixinmingpian(self):
        u'''查看微信名片'''
        self.d(text=u"我的").click()
        time.sleep(3)
        self.d(text=u"待完善").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_tv_right03").click()
        time.sleep(2)
        self.d.click(0.517, 0.955)
        time.sleep(2)


    def test04Xiugaiziliao(self):
        u'''修改个人资料'''
        self.d(text=u"我的").click()
        time.sleep(2)
        self.d(text=u"待完善").click()
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/ll_contact_mobile_phone").click()
        time.sleep(2)
        self.d(text=u"编辑").click()
        time.sleep(2)
        self.d.swipe(0.474, 0.944, 0.482, 0.263)
        time.sleep(2)
        self.d.click(0.541, 0.944) #点击保存键
        time.sleep(1)

    def test05Shezhi(self):
        u'''遍历个人资料菜单'''
        self.d(text=u"我的").click()
        time.sleep(2)
        self.d.click(0.916, 0.064)
        time.sleep(1)
        self.d(text=u"服务协议").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_title_left").click()
        time.sleep(1)
        self.d(text=u"隐私政策").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_title_left").click()
        time.sleep(1)
        self.d(text=u"版本说明").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.d(text=u"密码安全").click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)

    def test06ChangePWD(self):
        u'''修改密码测试'''
        self.d(text=u"我的").click()
        time.sleep(2)
        self.d.click(0.916, 0.064)
        time.sleep(1)
        self.d(text=u"密码安全").click()
        time.sleep(1)
        self.d(text=u"修改密码").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/old_pwd").click()
        time.sleep(1)
        self.d.send_keys("19851126")
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/new_pwd001").click()
        time.sleep(1)
        self.d.send_keys("19851126")
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/new_pwd002").click()
        time.sleep(1)
        self.d.send_keys("19851126")
        time.sleep(2)
        self.d.press("back")
        time.sleep(1)
        self.d(text=u"确认").click()
        time.sleep(1)





if __name__ == '__main__':
        unittest.main()
