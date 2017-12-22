# from appium import webdriver
# import time

# desired_caps = {
#     'platformName': 'Android', 
#     'platformVersion': '6.0', 
#     'deviceName': 'U10AFCPH235V8', 
#     'app': '', 
#     'appPackage': 'com.tencent.mm', 
#     'appActivity':'.ui.LauncherUI',
#     'unicodeKeyboard': False,
#     'resetKeyboard': False
# }



# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 
# driver.implicitly_wait(10)

from appium import webdriver
import selenium

import time
desired_caps = {
    'platformName': 'Android',
    'fastReset': False,
    'deviceName': 'U10AFCPH235V8',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'fullReset': False,
    'unicodeKeyboard': False,
    'resetKeyboard': False,
    'noReset':True,
    'androidProcess' : 'com.tencent.mm:tools' 
    }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.LinearLayout")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[3]")
el2.click()
el3 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"当前所在页面,我的收藏\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]")
el3.click()
# current = driver.current_context
# contexts = driver.contexts
# print("len:",len(contexts))
time.sleep(5)
print("slepp for 5 secound....")
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

driver.find_element_by_css_selector('div > ul:nth-child(3) > li:nth-child(1) > a').click()



