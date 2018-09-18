# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport
from public import log,cofig


class TestYituanma(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect_usb()
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
        self.log = log.log_message()
        self.d = self.u.session("com.esenyun.workline")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass

    def test01MyDaiban(self):
        self.log.info_log("我的待办")
        time.sleep(3)
        self.d(text=u"我的任务").click()
        time.sleep(1)
        self.d(text=u"新建").click()
        time.sleep(1)
        self.d.send_keys(u"123")
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_pony_more").click()  # 点击设置按钮
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/s_remind_switch").click()  # 选择指定时间提醒我
        time.sleep(1)
        self.d(description=u"27 九月 2018").click()  # 选择日期
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/mdtp_ok").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/mdtp_ok").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_verifier_hint").click()  # 添加验证人
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/contact_row_name", text=u"adsaf").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_confirm").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_executor").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_department", text=u"部部全").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_confirm").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_tv_right").click()  #测试提交2
        time.sleep(1)
        self.log.info_log("我的待办测试完成")  #ceshi
        time.sleep(2)
        self.assertTrue(self.d(resourceId="com.esenyun.workline:id/title_iv_right").exists, "控件定位不到")

    def test02Dashboard(self):
        self.log.info_log("进入数据看板")
        time.sleep(3)
        self.d(text=u"我的任务").click()
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right").click()
        time.sleep(4)
        self.d.click(0.513, 0.136) #点击我派发的任务
        time.sleep(1)
        self.d.click(0.816, 0.145) #点击带我验证
        time.sleep(1)
        self.d.press("back")
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right02").click()
        time.sleep(2)
        self.d(resourceId="com.esenyun.workline:id/tv_remind_time_hint").click()
        time.sleep(2)
        self.d(text=u"截止前15分钟").click()
        time.sleep(1)
        self.log.info_log("数据看板测试完成")
        time.sleep(1)
        self.assertTrue(self.d(resourceId="com.esenyun.workline:id/tv_remind_time_hint").exists, '测试失败')

    def test03MyPaifa(self):
        self.log.info_log("进入我的派发")
        time.sleep(1)
        self.d(text=u"我的任务").click()
        time.sleep(1)
        self.d(text=u"我派发的").click()
        time.sleep(1)
        self.d(text=u"新建").click()
        time.sleep(1)
        self.d.send_keys(u"321")
        time.sleep(1)
        self.d(text=u"确定").click()
        time.sleep(1)
        self.log.info_log("我的派发测试完成")
        time.sleep(1)
        self.assertTrue(self.d(text=u"新建").exists, "fail")

    def test04MyYanzheng(self):
        time.sleep(3)
        self.log.info_log("进入我的验证")
        self.d(text=u"我的任务").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_name", text=u"待我验证").click()
        time.sleep(1)
        self.d(text=u"已验证").click()
        time.sleep(1)
        self.d(text=u"已撤销").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/title_back").click()
        time.sleep(1)
        self.log.info_log("我的验证测试完成")
        time.sleep(1)
        self.assertTrue(self.d(text=u"新建").exists, "fail")



    def test05ZhuanRenwu(self):   #查看小白板数据
        time.sleep(3)
        self.log.info_log("小白板转任务测试开始")
        self.d(text=u"我的小白板").click()
        time.sleep(3)
        self.d(text=u"冷藏库开辟市场参考").click()
        time.sleep(3)
        self.d(text=u"转任务").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/iv_operator").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/contact_row_name", text=u"adsaf").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_confirm").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_confirm").click()
        time.sleep(1)
        self.log.info_log("小白板转任务测试完成")


    def test06Dianzan(self):
        time.sleep(3)
        self.d(text=u"我的小白板").click()
        time.sleep(3)
        self.d(text=u"冷藏库开辟市场参考").click()
        time.sleep(3)
        self.d(text=u"点赞").click()
        time.sleep(1)
        self.d(text=u"已赞").click()
        time.sleep(1)
        self.d(text=u"免打扰").click()
        time.sleep(1)
        self.d(text=u"通知").click()
        time.sleep(1)
        self.log.info_log("点赞测试完成")


    def test07CreateMOban(self): #生成个人模
        self.log.info_log("测试生成模板开始")
        time.sleep(3)
        self.d(text=u"我的小白板").click()
        time.sleep(3)
        self.d(text=u"冷藏库开辟市场参考").click()
        time.sleep(3)
        self.d(resourceId="com.esenyun.workline:id/title_iv_right02").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/tv_menu_title", text=u"生成个人模板").click()
        time.sleep(1)
        self.d(resourceId="com.esenyun.workline:id/md_buttonDefaultPositive").click()
        time.sleep(1)
        self.log.info_log("测试生成模板完成")
if __name__ == '__main__':
    unittest.main()
