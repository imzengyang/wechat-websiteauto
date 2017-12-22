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
报错信息为
```
[Chromedriver] Chromedriver exited unexpectedly with code null, signal SIGTERM
[Chromedriver] Changed state to 'stopped'
[Chromedriver] Error: chrome not reachable
  (Driver info: chromedriver=2.20.353145 (343b531d31eeb933ec778dbcf7081628a1396067),platform=Windows NT 10.0 x86_64)
    at Chromedriver.callee$2$0$ (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\appium-chromedriver\lib\chromedriver.js:197:15)
    at tryCatch (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:67:40)
    at GeneratorFunctionPrototype.invoke [as _invoke] (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:315:22)
    at GeneratorFunctionPrototype.prototype.(anonymous function) [as next] (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:100:21)
    at GeneratorFunctionPrototype.invoke (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:136:37)
 Error: chrome not reachable
  (Driver info: chromedriver=2.20.353145 (343b531d31eeb933ec778dbcf7081628a1396067),platform=Windows NT 10.0 x86_64)
    at Chromedriver.callee$2$0$ (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\appium-chromedriver\lib\chromedriver.js:197:15)
    at tryCatch (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:67:40)
    at GeneratorFunctionPrototype.invoke [as _invoke] (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:315:22)
    at GeneratorFunctionPrototype.prototype.(anonymous function) [as next] (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:100:21)
    at GeneratorFunctionPrototype.invoke (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:136:37)
[MJSONWP] Encountered internal error running command: Error: chrome not reachable
  (Driver info: chromedriver=2.20.353145 (343b531d31eeb933ec778dbcf7081628a1396067),platform=Windows NT 10.0 x86_64)
    at Chromedriver.callee$2$0$ (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\appium-chromedriver\lib\chromedriver.js:197:15)
    at tryCatch (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:67:40)
    at GeneratorFunctionPrototype.invoke [as _invoke] (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:315:22)
    at GeneratorFunctionPrototype.prototype.(anonymous function) [as next] (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:100:21)
    at GeneratorFunctionPrototype.invoke (C:\Users\zengyang\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\node_modules\babel-runtime\regenerator\runtime.js:136:37)
```
