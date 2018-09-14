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




    def test01TuanduiKanban(self):
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_img_right").click() #进入团队数据看板
        time.sleep(3)
        self.d.press("back")

    def test02InterMessage(self):
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(text=u"消息").click()  # 进入消息
        time.sleep(2)
        self.assertTrue(self.d(resourceId="com.esenyun.workline:id/buttonAudioMessage").exists,"未进入消息")
        time.sleep(2)

    def test03CreatTuandui(self):
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(text=u"新建").click()  # 开始新建团队
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/et_name").set_text("测试团队")
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/et_desc").set_text("测试测试测试测试(；′⌒`)")
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/iv_group_logo_right").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_dialog_item_name", text=u"从相册选择").click()
        time.sleep(1)
        self.d.click(0.077, 0.22)
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/done").click()
        time.sleep(1)
        self.d(resourceId="com.android.gallery3d:id/head_select_right", description=u"确定",
               className="android.widget.ImageButton", instance=1).click()
        time.sleep(1)
        self.d(text=u"完成并创建").click()
        time.sleep(1)




if __name__ == '__main__':
        unittest.main()
