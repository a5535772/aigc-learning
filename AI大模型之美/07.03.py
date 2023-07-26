import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

embedding_df = pd.read_parquet("data/20_newsgroup_with_embedding.parquet")

matrix = np.vstack(embedding_df.embedding.values)
num_of_clusters = 20

kmeans = KMeans(n_clusters=num_of_clusters, init="k-means++", n_init=10, random_state=42)
kmeans.fit(matrix)
labels = kmeans.labels_
embedding_df["cluster"] = labels

# 统计每个cluster的数量
new_df = embedding_df.groupby('cluster')['cluster'].count().reset_index(name='count')

# 统计这个cluster里最多的分类的数量
# 对 "embedding_df" 数据框按照 "cluster" 和 "title" 进行分组，统计每个 "cluster" 中每个 "title" 出现的次数
title_count = embedding_df.groupby(['cluster', 'title']).size().reset_index(name='title_count')
# 对 "title_count" 数据框按照 "cluster" 进行分组，获取每个 "cluster" 中 "title_count" 列值最大的行
first_titles = title_count.groupby('cluster').apply(lambda x: x.nlargest(1, columns=['title_count']))
# 重置 "first_titles" 数据框的索引
first_titles = first_titles.reset_index(drop=True)
# 将 "first_titles" 数据框的 "cluster"、"title"、"title_count" 列与 "new_df" 数据框按照 "cluster" 进行左连接
new_df = pd.merge(new_df, first_titles[['cluster', 'title', 'title_count']], on='cluster', how='left')
# 重命名 "new_df" 数据框中的 "title"、"title_count" 列为 "rank1"、"rank1_count"
new_df = new_df.rename(columns={'title': 'rank1', 'title_count': 'rank1_count'})

# 统计这个cluster里第二多的分类的数量
second_titles = title_count[~title_count['title'].isin(first_titles['title'])]
second_titles = second_titles.groupby('cluster').apply(lambda x: x.nlargest(1, columns=['title_count']))
second_titles = second_titles.reset_index(drop=True)
new_df = pd.merge(new_df, second_titles[['cluster', 'title', 'title_count']], on='cluster', how='left')
new_df = new_df.rename(columns={'title': 'rank2', 'title_count': 'rank2_count'})
new_df['first_percentage'] = (new_df['rank1_count'] / new_df['count']).map(lambda x: '{:.2%}'.format(x))
# 将缺失值替换为 0
new_df.fillna(0, inplace=True)
# 输出结果
from IPython.display import display

display(new_df)
