let chrome = require('selenium-webdriver/chrome');

let { Builder } = require('selenium-webdriver');

let driver = new Builder().
    usingServer('http://localhost:4723/wd/hub').
    withCapabilities({
        platformName: 'Android',
        platformVersion: '6.0',
        deviceName: 'U10AFCPH235V8',   //魅族设备 U10
        appPackage: "com.tencent.mm",
        appActivity: ".ui.LauncherUI",
        fastReset: false,
        fullReset: false,
        noReset: true,
        androidProcess: 'com.tencent.mm:tools',
        browserName: 'com.tencent.mm'
    }).
    build();
driver.sleep(10000);
driver.findElement({ xpath: "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.LinearLayout" }).click();
driver.findElement({xpath:"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[3]"}).click()
driver.findElement({xpath:"//android.widget.FrameLayout[@content-desc=\"当前所在页面,我的收藏\"]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]"}).click();
driver.sleep(10000)
driver.getPageSource().then(function(src){
    console.log("src=>")
})
driver.switchTo().activeElement("WEBVIEW_com.tencent.mm:tools")
