# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '26/10/2018 11:21 PM'

import requests
import json
import pandas as pd
import csv

cookies = {
    'UniqueID': 'xfxbgZKQTNlC0laj1534566549004',
    'Sites': '_21',
    '_ga': 'GA1.3.1038745649.1534566546',
    '_gid': 'GA1.3.1604362988.1534566546',
    '21_vq': '15',
}

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

# 处理三位数的补零
def add_zero(n):
    if len(str(n)) == 1:
        return '00' + str(n)
    elif len(str(n)) == 2:
        return '0' + str(n)
    elif len(str(n)) == 3:
        return str(n)

# 写入标题
with open('ssq.csv', 'w', encoding='utf-8-sig', newline='') as f:  # newline防止产生一行隔一行有空行的情况
    csv.writer(f).writerow(['期号', '开奖日期', '红球', '蓝球', '总销售额（元）', '奖池（元）', '一等奖中奖情况', '本期中奖情况'])

for q in range(1, 180):  # 每年基本在154期左右
    for y in range(2013, 2019):  # 从2013年到2018年
        params = (
            ('name', 'ssq'),
            ('issueCount', ''),
            ('issueStart', str(y) + add_zero(q)),
            ('issueEnd', str(y) + add_zero(q)),
            ('dayStart', ''),
            ('dayEnd', ''),
            ('pageNo', '')
        )
        url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice'
        response = requests.get(url=url, headers=headers, params=params, cookies=cookies)
        result = json.loads(response.text)['result']  # 得到返回的json数据
        df = pd.DataFrame(result, columns=['code', 'date', 'red', 'blue', 'sales', 'poolmoney', 'content', 'prizegrades'])
        if df.empty == 0:
            df.to_csv('ssq.csv', mode='a', encoding='utf_8_sig',index=0, header=0)
    print("历年第" + str(q) + "期抓取完成")