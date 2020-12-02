import requests
import re
from lxml import etree
success=""
num=0
lists=""
result_num_player_list=[]
result_num_comments_list=[]
url="https://www.bilibili.com/v/popular/rank/all/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}
bili = requests.get(url,headers=headers)
html = etree.HTML(bili.text)
result_title=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/a/text()')
result_url=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/a/@href')
result_score=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/div[@class="pts"]/div/text()')
result_num_player=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/div[@class="detail"]/span[@class="data-box"][1]/text()')
result_num_comments=html.xpath('//ul[@class="rank-list"]/li[@*]/div[@class="content"]/div[@class="info"]/div[@class="detail"]/span[@class="data-box"][2]/text()')
for temporary in result_num_player:
    temporary = temporary.strip()
    result_num_player_list.append(temporary)
for temporary in result_num_comments:
    temporary = temporary.strip()
    result_num_comments_list.append(temporary)
for title,play_num,score,comments_list,urls in zip(result_title,result_num_player_list,result_score,result_num_comments_list,result_url):
    num=num+1
    string_success=("排行榜第"+str(num)+"名:"+str(title)+"\n"+"综合得分"+str(score)+"    "+"播放量"+(play_num)+"    "+"评论数:"+(comments_list)+"\n"+"视频地址："+"https:"+str(urls))
    lists=(lists+string_success)
print(lists)
f = open("./bilibili_list.txt","w",encoding="utf-8")
f.write(lists)
f.close()
input("爬取完毕,按任意键退出")
