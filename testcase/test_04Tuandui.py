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
        self.d(text=u"新建").click() #开始新建团队
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
        time.sleep(2)
        self.assertTrue(self.d(text=u"测试团队").exists,"未找到新建的团队")
        time.sleep(1)



    def test04BianJiTeam(self):
        self.d(text=u"小白板", className="android.widget.TextView", instance=2).click()
        time.sleep(1)
        self.d.press("back")
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_pt_name", text=u"测试团队").click()  # 进入测试团队
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/trm_menu_item_text", text=u"认证为部门").click()
        time.sleep(3)
        self.d.click(0.153, 0.414)
        time.sleep(1)
        self.d.click(0.47, 0.852)
        time.sleep(1)
        self.d.click(0.563, 0.827)  # 认证为项目组成功
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right").click()  # 准备编辑团队资料
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/trm_menu_item_text").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/et_name").set_text("测试团队编辑资料测试")
        time.sleep(1)
        self.d(className="android.widget.RelativeLayout", instance=7).click()
        time.sleep(2)
        self.assertTrue(self.d(text=u"测试团队编辑资料测试").exists, "团队修改资料未成功")



    def test05DeleteTeam(self):
        self.d(text=u"团队").click()
        time.sleep(1)
        self.d(text=u"测试团队编辑资料测试").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/trm_menu_item_text", text=u"解散部门").click()
        time.sleep(1)
        self.d(text=u"确定").click()
        time.sleep(4)
        self.d.click(0.485, 0.829)  #点击确认通知按钮
        time.sleep(2)
        self.assertFalse(self.d(text=u"测试团队编辑资料测试").exists,"测试团队仍存在")
        time.sleep(2)





if __name__ == '__main__':
        unittest.main()
