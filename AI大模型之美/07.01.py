# 导入fetch_20newsgroups函数和pandas库
from sklearn.datasets import fetch_20newsgroups
import pandas as pd


# 定义函数twenty_newsgroup_to_csv
def twenty_newsgroup_to_csv():
    # 获取训练数据并移除头部、尾部和引用
    newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
    # 将数据转换为Pandas DataFrame格式，并添加两列，分别是文本和目标
    df = pd.DataFrame([newsgroups_train.data, newsgroups_train.target.tolist()]).T
    df.columns = ['text', 'target']
    # 将目标名称转换为Pandas DataFrame格式
    targets = pd.DataFrame(newsgroups_train.target_names, columns=['title'])
    # 将目标名称和目标ID进行合并，最后将结果保存到CSV文件中
    out = pd.merge(df, targets, left_on='target', right_index=True)
    out.to_csv('data/20_newsgroup.csv', index=False)


# 调用函数twenty_newsgroup_to_csv
twenty_newsgroup_to_csv()
