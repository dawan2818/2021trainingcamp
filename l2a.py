# -*- coding :  UTF-8 -*-
# 开发人员 :  wanda
# 开发时间 :  2021/2/8 上午 8:40
# 文件名称 :  l2a.PY
# 开发工具 :  PyCharm
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取网页数据，用BeautifulSoup导入
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html = requests.get(url, headers=headers, timeout=10)
content = html.text
soup = BeautifulSoup(content, 'html.parser')
# 获取投诉表格中的数据，并按行分开
table = soup.table
tr_list = table.find_all('tr')
# 每次循环将信息保存在临时表temp_list中，将其作为df表的一行记录，最终得到df表
df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
index = 0
for tr in tr_list[1:]:
    td_list = tr.find_all('td')
    temp_list = []
    for td in td_list[:-1]:
        temp_list.append(str(td.string))
    temp_list.append(str(tr.em.string))
    df.loc[index] = temp_list
    index += 1
# 将df表转化为Excel文件输出
df.to_excel('car_complain.xlsx', index=False)
