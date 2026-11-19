import pandas as pd
import jieba
from joblib import dump
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

train_data = pd.read_csv('assets/dataset/dataset.csv', sep='\t', header=None)

cn_stopwords = pd.read_csv('assets/dataset/baidu_stopwords.txt', header=None)[0].values
# jieba.lcut(text) 按照jieba分词规则对text进行分词，返回一个list
train_data[0] = train_data[0].apply(lambda x: " ".join([x for x in jieba.lcut(x) if x not in cn_stopwords]))

tfidf = TfidfVectorizer(ngram_range = (1,1) )
# fit_transform()：训练模型并返回训练数据的TF-IDF矩阵
train_tfidf = tfidf.fit_transform(train_data[0])

model = LinearSVC()
model.fit(train_tfidf, train_data[1])

# 变量保存
dump((tfidf, model), "./assets/weights/tfidf_ml.pkl") # pickle 二进制