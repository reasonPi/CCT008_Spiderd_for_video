# -*-coding:utf-8 -*- 
import requests
from requests.exceptions import RequestException
import re
import json
import time
import csv

def get_one_page(url):

    try:
        headers = {
        'Cookie': '_ga=GA1.3.652883885.1527396262; *************df9554bbfe647bed8d077615a930d25291530710334; ASP.NET_SessionId=rsnre345np02d445mbv3on45; VZr4_2132_ulastactivity=3838lgWQcXk5Da5JzBUp%2BRWVvM9hxTeobc4OxFuye6BNtiUJOJdp; VZr4_2132_auth=4dcdr7D48BY32F6QLYEkjHJEmtsHj8w5n%2FmGsFDTv9CgRsTxBX8YX84LEuXDacRWqsrbBOoWAw%2FUp9A4h2v%2F21e1vw; VZr4_2132_lastcheckfeed=14518%7C1530926541; VZr4_2132_sid=Hla6MX; VZr4_2132_lip=111.113.217.216%2C1530927316; VZr4_2132_st_p=14518%7C1530927358%7C9910ba07ccb0ebd3be0b25027bda73a1; VZr4_2132_visitedfid=20D10D31; VZr4_2132_viewid=tid_20698; VZr4_2132_sendmail=1; VZr4_2132_lastact=1530927359%09misc.php%09patch',
        'Host': 'utalk.xjtlu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None

def analyze_one_page(html):
    pattern = re.compile('onclick="atarget\(this\)" class="s xst">(.*?)</a>.*?<em><span>(.*?)</span></em>.*?<td class="num"><.*?class="xi2">(.*?)</a><em>(.*?)</em></td>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'name': item[0],
            'date': item[1],
            'value': item[2],
            'type': item[3],
        } 

def write_to_file(content):
    with open ('C:\\Users\\reasonPi\\Desktop\\data.csv', 'a', encoding='GBK') as csvfile:
        fieldnames = ['name', 'type', 'value', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(content)

def main(offset):
    url = 'http://utalk.xjtlu.edu.cn/forum/forum.php?mod=forumdisplay&fid=10&page=' + str(offset)
    html = get_one_page(url)
    for item in analyze_one_page(html):
        write_to_file(item)
        print(item)

if __name__ == '__main__':
    for i in range(4):
        main(offset=i)
        time.sleep(1)

