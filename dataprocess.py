import json
import os
import pandas as pd
import csv

FILE_NAME="maoyan2.csv"
class DataProcess(object):


    def __init__(self):

        self.file = open(FILE_NAME, "w", encoding="utf-8")
        self.file.close()

    # 读取文件
    def get_data(self, json_comment):
        json_response = json_comment["cmts"]  # 列表
        list_info = []
        for data in json_response:
            cityName = data["cityName"]
            content = data["content"]
            if "gender" in data:
                gender = data["gender"]
            else:
                gender = 0
            nickName = data["nickName"]
            userLevel = data["userLevel"]
            score = data["score"]
            time = data["startTime"]
            list_one = [time, nickName, gender, cityName, userLevel, score, content]
            list_info.append(list_one)
        self.file_do(list_info)

    # 存储文件
    def file_do(self,list_info):
        # 获取文件大小

        file_size = os.path.getsize(FILE_NAME)
        if file_size == 0:
            # 表头
            name = ['评论日期', '评论者昵称', '性别', '所在城市', '猫眼等级', '评分', '评论内容']
            # 建立DataFrame对象
            file_test = pd.DataFrame(columns=name, data=list_info)
            # 数据写入
            file_test.to_csv(FILE_NAME, encoding='utf-8', index=False)
        else:
            with open(FILE_NAME, 'a+', newline='',encoding='utf-8') as file_test:
                # 追加到文件后面
                writer = csv.writer(file_test)
                # 写入文件
                writer.writerows(list_info)
    def laststarttime(self):
        with open(FILE_NAME,'r', newline='',encoding='utf-8') as csvfile:
            targetLine = csvfile.readlines()[-1]
            a = targetLine.split(',')[0]
            return a
