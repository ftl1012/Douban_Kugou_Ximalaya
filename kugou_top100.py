import time
import json
from bs4 import BeautifulSoup
import requests


class Kugou(object):
    def __init__(self):
        self.header = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }

    def getInfo(self, url):
        html = requests.get(url, headers=self.header)
        soup = BeautifulSoup(html.text, 'html.parser')
        # print(soup.prettify())
        ranks = soup.select('.pc_temp_num')
        titles = soup.select('.pc_temp_songlist > ul > li > a')  # 层层标签查找
        times = soup.select('.pc_temp_time')
        for rank, title, songTime in zip(ranks, titles, times):
            data = {
                # rank 全打印就是带HTML标签的
                'rank': rank.get_text().strip(),
                'title': title.get_text().split('-')[1].strip(),
                'singer': title.get_text().split('-')[0].strip(),
                'songTime': songTime.get_text().strip()
            }
            s = str(data)
            print('rank:%2s\t' % data['rank'], 'title:%2s\t' % data['title'], 'singer:%2s\t' %data['singer'], 'songTime:%2s\t' % data['songTime'])
            with open('hhh.txt', 'a', encoding='utf8') as f:
               f.writelines(s + '\n')

if __name__ == '__main__':
    urls = [
        'http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(2)
    ]

    kugou = Kugou()
    for url in urls:
        kugou.getInfo(url)
        time.sleep(1)



