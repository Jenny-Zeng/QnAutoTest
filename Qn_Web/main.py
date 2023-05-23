import calendar
import hashlib
from sched import scheduler
import threading
import time
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import base64
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
#from wechat import Robot
from pathlib import Path

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 1,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 1,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 1         # 1:allow, 2:block 
})

driver = webdriver.Chrome(chrome_options=options)
current_milli_time = lambda: int(round(time.time() * 1000))
driver.get("https://demo-rtc.qnsdk.com/")
driver.maximize_window()
# 输入内容前先进行清空操作
qw = driver.find_element(By.TAG_NAME,"input").clear()
# # 获取用户名文本框大小
driver.find_element(By.TAG_NAME,"input").send_keys("zeng")
driver.find_element(By.CLASS_NAME,"home_btn").click()
room = calendar.timegm(time.gmtime())
driver.find_element(By.TAG_NAME,"input").send_keys(room)
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#root > div > div.jss31 > div > div:nth-child(4) > div > button").click()
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[3]/button/span[1]").click() 
   
def screenshot( ): 
    sleep(5) 
    driver.get_screenshot_as_file('./pictures/bug.png')
    with open('./pictures/bug.png','rb') as f:
        base64_data = base64.b64encode(f.read())    
        image_data = str(base64_data,'utf-8')
    with open('./pictures/bug.png','rb') as f:
        # 获取图片的md5值
        md = hashlib.md5()
        md.update(f.read())
        image_md5 = md.hexdigest()
    # 企业微信机器人发送图片消息
    #url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=95c11ebb-a329-4695-b450-d7e3a5e01649'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=640012ea-3fed-4f3f-86fd-9d672860121f'
    headers = {"Content-Type":'application/json'}
    data = {
        'msgtype':'image',
        'image':{
            'base64':image_data,
            'md5':image_md5
        }
    }
    r = requests.post(url,headers=headers,json=data,)

##定时器：每隔1分钟截图一次
def timescreen():
    threading.Timer(5,screenshot).start() 
    
# if __name__ == '__main__':
#     timescreen()

#     sleep(60)
#every(10).second.do(screenshot,"10s")
sleep(60)
    


        