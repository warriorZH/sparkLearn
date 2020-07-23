#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: __main__.py
#description: package main entrance
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-18
#log:
from pyspark import SparkContext
import commands
from sparkClusterAlgorithm import *
from wordSeg import *

print('__main__')
print('__main__.__name__', __name__)
print('__main__.__package__', __package__)




sc = SparkContext(appName="newsCluster")
sc.addPyFile("/home/warrior/gitDir/pysparkCode/clusterNews/wordSeg.py")
sc.addPyFile("/home/warrior/gitDir/pysparkCode/clusterNews/sparkClusterAlgorithm.py")
wordseg = wordSeg()
clustermanage = sparkClusterAlgorithm()
files = sc.wholeTextFiles("hdfs://warrior:9000/testData/skynews")
files_num = files.collect()
print len(files_num)
file_list = files.map(lambda item: item[1])
file_wc_dict_list = file_list.map(lambda file_content:wordseg.GetWordCountTable(file_content))
file_wc_dict_list.persist()
file_wc_dict_list_result = file_wc_dict_list.collect()
all_word_dict = wordseg.updateAllWordList(file_wc_dict_list_result)#file_wc_dict_list.map(lambda file_wc_dict:wordseg.updateAllWordList(file_wc_dict))
all_word_result = all_word_dict
# print len(all_word_result)
file_feature_dict_list = file_wc_dict_list.map(lambda file_wc_dict: wordseg.constructFeatureDict(file_wc_dict, all_word_result))
file_feature_dict_result = file_feature_dict_list.collect()
#main本地运行模式
# k_class_sample_record = []
# for item in file_feature_dict_result:
#     k_class_sample_record.append(clustermanage.K_MeansCluster(clustermanage.calcu_cosine_corr, item, file_feature_dict_result, 4))


k_class_sample_record = file_feature_dict_list.map(lambda file_feature_dict:clustermanage.K_MeansCluster(clustermanage.calcu_cosine_corr, file_feature_dict, file_feature_dict_result, 4))
# k_class_sample_record.saveAsTextFile("hdfs://warrior:9000/testData/KClassRecordResult")
# status, results = commands.getstatusoutput("hadoop fs -cat hdfs://warrior:9000/testData/KClassRecordResult/part-00000")
# print results
# status, results = commands.getstatusoutput("hadoop fs -rmr hdfs://warrior:9000/testData/KClassRecordResult")
# print results
k_class_sample_record_result = k_class_sample_record.collect()
print k_class_sample_record_result
# print len(file_feature_dict_result[0])
# print "hello!!"
sc.stop()
