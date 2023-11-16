import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains


#九宫格解锁
def movepoint(driver):
    print("unlock")
    print(driver.current_activity)
    # TouchAction(driver).press(285, 1031).move_to(285, 1031).move_to(795, 1587).release().perform()
    # driver.swipe(285, 1031, 795, 1031, 500)
    time.sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions.pointer_action.move_to_location(258, 931)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(795, 931)
    actions.w3c_actions.pointer_action.move_to_location(795, 1487)
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()

def loginhs(driver):
    print("login")
    # 点击搜索框

    driver.find_element(AppiumBy.ID, "login_ed_username").click()
    # 输入“泰坦尼克号”
    driver.find_element(AppiumBy.ID, "login_ed_username").send_keys("18")
    # driver.find_element_by_id("com.secure.client:id/login_ed_pwd").click()
    driver.find_element(AppiumBy.ID, "login_ed_pwd").click()
    # 输入“泰坦尼克号”
    driver.find_element(AppiumBy.ID, "login_ed_pwd").send_keys("qq123456.")
    driver.find_element(AppiumBy.ID, "login_pwd_eye").click()
    driver.find_element(AppiumBy.ID, "login_check").click()
    driver.find_element(AppiumBy.ID, "login_btn_login").click()
    if driver.current_activity == "com.yizhi.vpn.main.activity.FingerPrintActivity":
        print("jiugonggejiesuo")
        driver.find_element(AppiumBy.ID, "ly_ss").click()
    time.sleep(2)
    # driver.tap([(285, 1031), (285, 1031), (795, 1587)], 2000)
    # driver.flick(start_x=285, start_y=1031 ,end_x=795, end_y=1587)
    # driver.swipe(285, 1031, 795, 1031, 300)

#添加服务器地址
def addserver(driver):
    print("add address")
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "text_input_server").click()
    driver.find_element(AppiumBy.ID, "add_server").click()
    driver.find_element(AppiumBy.ID, "edit_server_address").click()
    driver.find_element(AppiumBy.ID, "edit_server_address").send_keys("118.116.4.12:48443")
    driver.find_element(AppiumBy.ID, "button_save_server_address").click()
    driver.find_element(AppiumBy.ID, "item_sa_server_address").click()
    driver.find_element(AppiumBy.ID, "button_connect").click()