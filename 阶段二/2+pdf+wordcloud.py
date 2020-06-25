# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿

import urllib
import importlib, sys

importlib.reload(sys)
import re
import jieba
import collections # 词频统计库
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import matplotlib.pyplot as plt
from wordcloud import WordCloud
plt.rcParams['font.sans-serif']=['SimHei']#中文显示
plt.rcParams['axes.unicode_minus'] = False
def parse(DataIO, save_path):
    parser = PDFParser(DataIO)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmagr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmagr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmagr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                try:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        with open('%s' % (save_path), 'a') as f:
                            result = x.get_text()
                            f.write(result + "\n")
                except:
                    print("Failed")


if __name__ == '__main__':
    # 解析本地PDF文本，保存到本地TXT
    # with open(r'Java实战入门.pdf', 'rb') as pdf_html:
    #     parse(pdf_html, r'Java实战入门.txt')
    with open('Java实战入门.txt','r',encoding='gbk') as f:
        mytext = f.readlines()
    # 文本预处理
    # pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    mytext = re.findall('[\u4e00-\u9fa5]', str(mytext))  # 将符合模式的字符去除
    mytext_str = ''.join(mytext)
    # 文本分词
    seg_list_exact = jieba.cut(mytext_str, cut_all=False)  # 精确模式分词
    object_list = []
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了',
                    u'通常', u'如果', u'我们', u'需要']  # 自定义去除词库

    for word in seg_list_exact:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            object_list.append(word)  # 分词追加到列表

    object_list_str = ''.join(object_list)
    # print(object_list_str)
    # 词频统计
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top15 = word_counts.most_common(15)  # 获取前15最高频的词
    print(word_counts_top15)  # 输出检查

    # mycloud = WordCloud(font_path='./fonts/simhei.ttf').generate(str(object_list))
    # plt.imshow(mycloud)
    # plt.axis('off')  # 关闭词云图坐标显示
    # plt.savefig('out.jpg', dpi=1000, edgecolor='blue', bbox_inches='tight', quality=95)  # 保存词云图（到工作路径下）
    # plt.show()

