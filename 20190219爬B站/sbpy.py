# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '11/2/2019 9:19 AM'


import requests
from fake_useragent import UserAgent
import json
import time
import pandas as pd

#下载网页评论数据
def get_page_json(url):
    try:
        ua = UserAgent(verify_ssl=False)
        headers = {"User-Agent": ua.random}
        json_comment = requests.get(url,headers=headers).text
        return json_comment
    except:
        return None

#解析网页评论数据
def parse_page_json(json_comment):
   try:
       comments = json.loads(json_comment)
   except:
       return "error"

   comments_list = []
   #获取当页数据有多少条评论（一般情况下为20条）
   num = len(comments['data']['replies'])

   for i in range(num):
       comment = comments['data']['replies'][i]
       comment_list = []
       floor = comment['floor']
       ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment['ctime']))#时间转换
       likes = comment['like']
       author = comment['member']['uname']
       sex = comment['member']['sex']
       level = comment['member']['level_info']['current_level']
       content = comment['content']['message'].replace('\n','')#将评论内容中的换行符去掉
       #print(content)
       rcount = comment['rcount']
       comment_list.append(floor)
       comment_list.append(ctime)
       comment_list.append(likes)
       comment_list.append(author)
       comment_list.append(sex)
       comment_list.append(level)
       comment_list.append(content)
       comment_list.append(rcount)

       comments_list.append(comment_list)

   save_to_csv(comments_list)


def save_to_csv(comments_list):
    data = pd.DataFrame(comments_list)
    #注意存储文件的编码为utf_8_sig，不然会乱码，后期会单独深入讲讲为何为这样（如果为utf-8）
    data.to_csv('春晚鬼畜_1.csv', mode='a', index=False, sep=',', header=False,encoding='utf_8_sig')


def main():
    base_url = "https://api.bilibili.com/x/v2/reply?&type=1&oid=19390801&pn=1"
    #通过首页获取评论总页数
    pages = int(json.loads(get_page_json(base_url))['data']['page']['count'])//20
    for page in range(pages):
        url = "https://api.bilibili.com/x/v2/reply?&type=1&oid=19390801&pn="+str(page)
        json_comment = get_page_json(url)
        parse_page_json(json_comment)
        print("正在保存第%d页" % int(page+1))

        if page%20 == 0:
            time.sleep(5)



main()