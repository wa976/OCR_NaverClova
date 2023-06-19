import matplotlib
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

#한글 표시를 위한 폰트
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

# 엑셀파일 불러오기
df = pd.read_excel('data.xlsx')


# 군집화 할 feature 선택
features = ['박스(개)','가격']
df_cluster = df[features]

# feature 정규화
scaler = StandardScaler()
df_cluster_scaled = scaler.fit_transform(df_cluster)

# K-mean 군집화
kmeans = KMeans(n_clusters=4)
kmeans.fit(df_cluster_scaled)

# 군집 label 설정
df['Cluster'] = kmeans.labels_

# 겹치는 point 방지를 위한 랜덤 변수 곱해주기
df['박스_(개)'] = df['박스(개)'] + 0.4 * np.random.rand(len(df))
df['가격_'] = df['가격'] + 10000 * np.random.rand(len(df))

# 반응형 그래프 생성
fig = px.scatter(df, x='가격_', y='박스_(개)', color='Cluster', hover_data=df.columns)

fig.show()

