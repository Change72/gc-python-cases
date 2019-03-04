# -*- coding=utf-8 -*-
import jieba    #分词包
import numpy    #numpy计算包
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
import pandas


file=codecs.open(u"../data/分节符的使用.txt",'r')
content=file.read()
file.close()
segment=[]
segs=jieba.cut(content) #切词，“么么哒”才能出现
for seg in segs:
    if len(seg)>1 and seg!='\r\n':
        segment.append(seg)
#print(segment)
words_df=pandas.DataFrame({'segment':segment})
words_df.head()
#print(words_df)
stopwords=pandas.read_csv("../data/stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding="gb2312")
#print(stopwords)
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
#print(words_df)
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
#print(words_stat)
#words_stat=words_stat.reset_index().sort(columns="计数",ascending=False)
print(words_stat)
