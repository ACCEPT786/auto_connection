from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import signal
import os

current_path = os.getcwd()


def install_git():
    result = os.system("git --version")
    if result != 0:
        os.system("brew install git")


def check_and_connect():
    while True:
        return1 = os.system('ping -c2 www.baidu.com')
        if return1:
            username_str = "2125919"  # 你的校园网登陆用户名
            password_str = "135798642CY"  # 你的校园网登陆密码
            driver = webdriver.Firefox(executable_path=current_path + "/geckodriver")
            can_connect = True
            driver.get("http://login.wku.edu.cn/ac_portal/default/pc.html?tabs=pwd")  # 你的校园网登陆地址
            time.sleep(3)
            username_input = driver.find_element_by_id("password_name")  # 校园网登陆用户名的输入控件ID, 浏览器上右键查看网页源代码查询
            password_input = driver.find_element_by_id("password_pwd")  # 校园网登陆密码的输入控件ID, 浏览器上右键查看网页源代码查询
            print('Searching connect')
            login_button = driver.find_element_by_id("password_submitBtn")  # 校园网登陆连接的点击控件ID, 浏览器上右键查看网页源代码查询
            print('Find connect successfully')
            username_input.send_keys(username_str)
            password_input.send_keys(password_str)
            print('Input user info')
            login_button.click()
            print('Connect')
            driver.close()
            time.sleep(10)
        else:
            print("Connected")
            time.sleep(10)


judge = os.path.exists(current_path + "/geckodriver")
if judge:
    print("file exist")
    install_git()
    check_and_connect()
else:
    print("file not exist")
    install_git()
    os.system("git clone https://github.com/ACCEPT786/geckodriver.git " + current_path + "/geckodriver")
    check_and_connect()
