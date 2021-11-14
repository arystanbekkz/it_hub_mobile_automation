import os
from appium import webdriver

def before_scenario(context, scenario):

    desired_cap = {"deviceName": "Nexus6P", "platformName": "Android", "app": os.path.abspath(
                        os.path.abspath
                         ("C:/Users/aryst/Documents/Обучение/Тестирование/Тестирование HomeCredit/9-10 занятие/white_test.apk")

                         ), "appPackage": "kz.homecredit.ibank.debug", "appActivity": (
             "cz.bsc.mb.activities.prelogin.SplashScreenActivity"
         ), "newCommandTimeout": 6000}

    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


def after_scenario(context, scenario):
    context.driver.quit()
