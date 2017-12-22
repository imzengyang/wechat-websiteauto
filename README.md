# wechat-websiteauto
遇到的一些坑，填不满


## 分别写了一个 node.js 和python 版本的 微信端浏览器自动化例子 （没成功）


## 思路
使用appium 驱动Android 手机， 实现手机端的自动化测试，
1 appium 打开Android版本微信，点击  我--我的收藏--点击收藏的页面（native端）
2 切换webview 进行web自动化

### 环境
- node.js:  v8.9.1
- selenum-webdriver: 3.6.0 
- chromedriver: 2.34.0
- appium: 1.7.1
---
- python:3.6.4
- python-selenium  `pip install -U selenium` https://pypi.python.org/pypi/selenium
- python-appium : `pip install appium-client`    github:https://github.com/appium/python-client

### 过程
参考 https://testerhome.com/topics/6954，
##### 1 使用node.js,  
脚本参考index.js 文件，实现了微信native端自动化 ，却发现selenium-webdriver的api 没有提供切换webview 的方法 https://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/webdriver_exports_TargetLocator.html


#### 2. 使用python
参考 index.py, 使用 `driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')` 切换webview 是不好使，参考`https://testerhome.com/topics/8990`  chromedriver 降级到2.20 也不好使。
