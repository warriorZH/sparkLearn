#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: wordSeg.py
#description: example code for k-means to cluster text file in spark
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-18
#log:
import commands
import re
import clusterAlgorithm
import wordSeg


if __name__ == "__main__":
    wordseg = wordSeg.wordSeg()
    clustermanage = clusterAlgorithm.clusterAlgorithm()
    file_path = "/home/warrior/Desktop/skynews/"
    status, ls_results = commands.getstatusoutput("ls "+file_path)
    p = re.compile('''\w+''')
    file_name_list = p.findall(ls_results)
    #print file_name_list
    #获取文件内容，按文件存入一个list
    file_content_list = []
    for item in file_name_list:
        fd = open(file_path+item,'r')
        file_content_list.append(fd.read())
        fd.close()
    #将对应文章进行词频统计，并以word--count形式存储，然后整篇文章仍旧以list存储
    file_word_dict_list = []
    for item in file_content_list:
        file_word_dict_list.append(wordseg.GetWordCountTable(item))
    #建立一个包含所有文章词汇的字典
    all_word_dict = wordseg.updateAllWordList(file_word_dict_list)
    #建立对应文章的词频特征
    file_feature_dict_list = []
    for item in file_word_dict_list:
        file_feature_dict_list.append(wordseg.constructFeatureDict(item, all_word_dict))

    # #初选k个类作为初始类中心
    # k_class_centre = file_feature_dict_list[0:4]
    # #进行一次迭代，并记录下每篇文章属于哪个类，
    # #k_class_record这个list的index索引与file_feature_dict_list的文章索引相对应，对应索引上的值表示该文章属于哪个类
    # k_class_record = []
    # for item in file_feature_dict_list:
    #     k_class_record.append(clustermanage.once_K_MeansCluster(clustermanage.calcu_cosine_corr,item, k_class_centre, 4))
    # print k_class_record

    clustermanage.K_MeansCluster(clustermanage.calcu_cosine_corr, file_feature_dict_list, 4, 2, 20)
    print clustermanage.cluster_class_sample_record

    print "hello!!"
