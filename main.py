from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import time

import os
from flask import Flask
app=Flask(__name__)
@app.route('/')


def initLogin():
    url='http://jwstudent.lnu.edu.cn/login'
    option=webdriver.ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('headless')
    browser=webdriver.Chrome(options=option)
    browser.get(url)
    browser.set_window_size(600,800)
    return browser


def loginSite(browser):
    try_time=0
    wrong_checkcode="Checkcode Wrong!"
    while(1):
        try:
            input_id = browser.find_element(by=By.ID, value='input_username')
        except:
            break
        else:
            if(try_time):
                print(wrong_checkcode)
            time.sleep(2)
            input_id=browser.find_element(by=By.ID,value='input_username')
            input_pswd=browser.find_element(by=By.ID,value='input_password')
            input_checkcode=browser.find_element(by=By.ID,value='input_checkcode')
            btn_submit=browser.find_element(by=By.ID,value='loginButton')
            img_captcha=browser.find_element(by=By.ID,value="captchaImg")

            img=Image.open(BytesIO(img_captcha.screenshot_as_png))
            img.save('captchaImg.png')

            #id=input()
            #pswd=inut()
            id='20202091116'
            pswd='Pander1234'
            checkcode=input()

            input_id.send_keys(id)
            input_pswd.send_keys(pswd)
            input_checkcode.send_keys(checkcode)

            btn_submit.click()
            time.sleep(1)
            try_time+=1


def fetchCourseTable(browser):
    url='http://jwstudent.lnu.edu.cn/student/courseSelect/thisSemesterCurriculum/index'
    list_coursetable=[]
    col=7
    browser.get(url)
    time.sleep(1)

    coursetable=browser.find_element(by=By.ID,value='courseTable')
    coursetablecontect=coursetable.find_elements(by=By.TAG_NAME,value='td')
    for i in coursetablecontect:
        list_coursetable.append(i.text)
    lst=[list_coursetable[i:i + col] for i in range(0, len(list_coursetable), col)]
    for i in range(1,6):
        lst.pop(i)

    for i in lst:
        print(i)


def login():
    browser=initLogin()
    loginSite(browser)
    fetchCourseTable(browser)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)

