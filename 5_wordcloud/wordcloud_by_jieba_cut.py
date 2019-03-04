import os
import jieba
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator


filename = '大话西游.txt'
background_name = 'fruit.jpg'
word_file = 'words.txt'

def strip_word():
    # 第一次运行程序时将分好的词存入文件
    words = ''
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip('\n')
            words += ' '.join(jieba.cut(line))
            words += ' '
    file.close()
    # 写入磁盘
    writer = open(word_file,'wb')
    pickle.dump(words, writer)
    writer.close()


def draw_plot():
    # 直接从文件读取数据
    words = pickle.load(open(word_file,'rb'))
    backgroud_Image = plt.imread(background_name)
    wc = WordCloud( background_color = 'white',    # 设置背景颜色
                    mask = backgroud_Image,        # 设置背景图片
                    max_words = 50,                # 设置最大现实的字数
                    stopwords = STOPWORDS,         # 设置停用词
                    font_path = './fonts/simhei.ttf',# 设置字体格式，如不设置显示不了中文
                    max_font_size = 1000,          # 设置字体最大值
                    random_state = 30,             # 设置有多少种随机生成状态，即有多少种配色方案
                    )
    wc.generate(words)
    image_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func = image_colors)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    if not os.path.exists(word_file):
        strip_word()
    draw_plot()