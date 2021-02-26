# _*_ coding : UTF-8 _*_
# 开发人员 : wanda
# 开发时间 : 2021/2/26 下午 2:17
# 文件名称 : l3a.py
# 开发工具 : PyCharm
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

data = pd.read_csv('car_data.csv', encoding='gbk', )
train_x = data[['人均GDP', '城镇人口比重', '交通工具消费价格指数', '百户拥有汽车量']]
kmeans = KMeans(n_clusters=3)
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
data['分类'] = predict_y
print('分类后数据如下：')
print(data)