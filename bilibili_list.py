import requests
from lxml import etree
success=""
num=0
lists=""
url="https://www.bilibili.com/v/popular/rank/all/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}
bili = requests.get(url,headers=headers)
html = etree.HTML(bili.text)
result_title=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/a/text()')
result_score=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()')
result_num=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()')

for title,score in zip(result_title,result_num):
    num=num+1
    success=("排行榜第"+str(num)+"名:"+str(title)+"\n"+"综合得分"+str(score)+"\n")
    lists=(lists+success)
input("爬取完毕,按任意键退出")
f = open("./bilibili_list.txt","w",encoding="utf-8")
f.write(lists)
f.close()
