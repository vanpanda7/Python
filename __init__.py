# -*- coding: utf-8 -*-
import xlsxwriter as xw
import  requests
import  re
import  json
import  time
import  pprint
from urllib import request
import random

# url_html1 = 'https://api.bilibili.com/pgc/review/short/list?media_id=4315402&ps=20'
# 短评
url_html1 = 'https://api.bilibili.com/pgc/review/short/list?media_id=4315402&ps=20&cursor='
# 长评
url_html2 = 'https://api.bilibili.com/pgc/review/short/list?media_id=4315402&ps=20&cursor='

global x,url,num
x = 10000
url = url_html2
num=[]
allnum = 0

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
temp = 'buvid3=D0E81D21-FDEB-7BD5-6F7D-2C47E706366A26437infoc; b_nut=1665204926; i-wanna-go-back=-1; b_ut=5; _uuid=C7E54D95-4B66-A897-4D510-52FF35210A57E27690infoc; buvid_fp=a4129ba7e787907d042b5af64c89a5db; buvid4=D2D1D71F-32F4-7542-0677-DA71B2ECA4C728183-022100812-YyeQqvp3XSOoX3CaUB5r+Q%3D%3D; fingerprint=a4129ba7e787907d042b5af64c89a5db; buvid_fp_plain=undefined; SESSDATA=557cd98e%2C1688470503%2Cd36b2%2A11; bili_jct=782440ecc6d00851edf13be5a9bbeed1; DedeUserID=175878648; DedeUserID__ckMd5=6f7cf02b122a299b; sid=7pfhwuer; CURRENT_FNVAL=4048; blackside_state=1; rpdid=|(J|~|YlYRu|0J\'uYYmlYm)~~; innersign=1; b_lsid=7DFB10C86_18581B6857E'
cookie_list = temp.split(';')
cookies = {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookie_list}

proxy_list = [
  {"http":"113.100.209.123"},
  # {"http":"202.109.157.61"},
  {"http":"202.109.157.60"},
]
proxy = random.choice(proxy_list)

def doReq(cursorx):
    try:
        global x,url,num,allnum
        x = x - 1
        urls = url + cursorx
        response = requests.get(urls, headers=headers,cookies=cookies , proxies = proxy)
        json_data = json.loads(response.content)
        for i in range(len(json_data['data']['list'])):
            cursor = json_data['data']['next']
            mid = json_data['data']['list'][i]['author']['mid']
            vipName = json_data['data']['list'][i]['author']['vip_label']['text']
            content = json_data['data']['list'][i]['content']
            ctime = json_data['data']['list'][i]['ctime']
            try:
                progress = json_data['data']['list'][i]['progress']
            except:
                progress = "无"
            likes = json_data['data']['list'][i]['stat']['likes']
            score = json_data['data']['list'][i]['score']

            now = int(ctime)
            # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
            timeArray = time.localtime(now)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            insertData = [mid,vipName,content,progress,otherStyleTime,likes,score]
            row = 'A' + str(i+2+allnum)
            worksheet1.write_row(row, insertData)
        allnum = allnum + len(json_data['data']['list'])
        print("已爬取数据:" + str(allnum))
        if (x != 0):
            doReq(str(cursor))
        else:
            print("完成！")
            workbook.close()  # 关闭表
    except Exception as err:
        print(err)
        workbook.close()  # 关闭表



workbook = xw.Workbook('短评.xlsx')  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
title = ['mid', 'vipName', 'content','progress', 'ctime', 'likes', 'score']  # 设置表头
worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
doReq("")
