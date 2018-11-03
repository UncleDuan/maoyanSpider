import requests
from fake_useragent import UserAgent
import json
import dataprocess
import time
import re
headers = {
        "User-Agent": UserAgent(verify_ssl=False).random,
        "Host":"m.maoyan.com",
        "Referer":"http://m.maoyan.com/movie/1203437/comments?_v_=yes"
    }
# 猫眼电影短评接口

offset_list=[15*index for index in range(67)]
print(offset_list)
dp = dataprocess.DataProcess()
startTime = ['2018','11','01','17','40','00']
endTime="2018-09-30 00:00:00"

while True:
    for offset in offset_list:

        comment_api = 'http://m.maoyan.com/mmdb/comments/movie/1203437.json?_v_=yes&offset={0}&startTime={1}-{2}-{3}%20{4}%3A{5}%3A{6}'.format(offset,startTime[0],startTime[1],startTime[2],startTime[3],startTime[4],startTime[5])

        # 发送get请求
        headers = {
            "User-Agent": UserAgent(verify_ssl=False).random,
            "Host": "m.maoyan.com",
            "Referer": "http://m.maoyan.com/movie/1203437/comments?_v_=yes"
        }
        response_comment = requests.get(comment_api,headers = headers)
        json_comment = response_comment.text
        json_comment = json.loads(json_comment)
        print(json_comment)
        dp.get_data(json_comment)
    #找到最后一个数据的starttime，更新到comment——api中
    startTime=dp.laststarttime()
    startTime=re.split(r'[-:\s]', startTime)


