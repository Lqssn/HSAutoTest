# 导入webdriver
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
import login
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.secure.client',  # 启动APP Package名称
    'appActivity': 'com.yizhi.vpn.main.activity.StartActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': False,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 设置等待时间，如果不给时间的话可能会找不到元素
driver.implicitly_wait(5)

#九宫格解锁
# def movepoint():
#     print("unlock")
#     print(driver.current_activity)
#     # TouchAction(driver).press(285, 1031).move_to(285, 1031).move_to(795, 1587).release().perform()
#     # driver.swipe(285, 1031, 795, 1031, 500)
#     time.sleep(2)
#     actions = ActionChains(driver)
#     actions.w3c_actions.pointer_action.move_to_location(258, 931)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(795, 931)
#     actions.w3c_actions.pointer_action.move_to_location(795, 1487)
#     actions.w3c_actions.pointer_action.pointer_up()
#     actions.perform()
#

#登录
# def loginhs():
#     print("login")
#     # 点击搜索框
#
#     driver.find_element(AppiumBy.ID, "login_ed_username").click()
#     # 输入“泰坦尼克号”
#     driver.find_element(AppiumBy.ID, "login_ed_username").send_keys("18")
#     # driver.find_element_by_id("com.secure.client:id/login_ed_pwd").click()
#     driver.find_element(AppiumBy.ID, "login_ed_pwd").click()
#     # 输入“泰坦尼克号”
#     driver.find_element(AppiumBy.ID, "login_ed_pwd").send_keys("qq123456.")
#     driver.find_element(AppiumBy.ID, "login_pwd_eye").click()
#     driver.find_element(AppiumBy.ID, "login_check").click()
#     driver.find_element(AppiumBy.ID, "login_btn_login").click()
#     if driver.current_activity == "com.yizhi.vpn.main.activity.FingerPrintActivity":
#         print("jiugonggejiesuo")
#         driver.find_element(AppiumBy.ID, "ly_ss").click()
#         movepoint()
#         movepoint()
    # driver.tap([(285, 1031), (285, 1031), (795, 1587)], 2000)
    # driver.flick(start_x=285, start_y=1031 ,end_x=795, end_y=1587)
    # driver.swipe(285, 1031, 795, 1031, 300)

#首次启动进行添加服务器、登录、设置九宫格解锁密
#添加服务器
login.addserver(driver)
# 暂停2s
time.sleep(2)
# 判断当前在登录界面或者是九宫格界面
if driver.current_activity == "com.yizhi.vpn.main.activity.LoginActivity":
    print("now login hs")
    #登录
    login.loginhs(driver)
    #设置九宫格解锁密码
    login.movepoint(driver)
    login.movepoint(driver)
else:
    print("now unlock hs")
    login.movepoint(driver)
#测试结束
input('finish testing')

driver.quit()
