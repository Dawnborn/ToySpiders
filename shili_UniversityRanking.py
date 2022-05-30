# 嵩天MOOC第二周6单元
import requests
import bs4
from bs4 import BeautifulSoup
import re
import lxml

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUniList(ulist, html):
    soup = BeautifulSoup(html, "lxml")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag): # 检测标签类型
            tds = tr('td')  # tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
            #ulist延长，格式为方括号中的形式，即学校的排名名称和分数
    pass

def printUniList(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'   # {3}表示使用format中3号元素进行填充
    print(tplt.format('排名', '学校', '分数', ' '))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    html = getHTMLText(url)
    fillUniList(uinfo, html)
    printUniList(uinfo, 20)

main()