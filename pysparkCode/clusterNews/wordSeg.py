#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: wordSeg.py
#description: segment for english news
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-14
#log:

import re
import commands
import collections
#********************-----------------********************#

#********************-----------------********************#
class wordSeg(object):
    '''
        segment for english news
        函数执行流程：
        生成词频表=》更新词典=》构建基于词频表的特征词典
    '''

    def __init__(self):
        pass
        # self.all_word_list = []
        # self.all_word_dict = {}

#-----------------********************-----------------#


#-----------------********************-----------------#
    def GetWordCountTable(self, readString):
        '''
            description: segment readString and construct word-count dict
            input:
                readString: the input file string to be segment and manage
            output:
                readWordCountDict: the last result of word-count dict for readString
        '''
        repattern = re.compile('''\w+''')
        readWordList = repattern.findall(readString)
        readWordCountDict = collections.Counter(readWordList) #获得词频统计词典 key:value
        return readWordCountDict

#-----------------********************-----------------#
    def updateAllWordList(self, newWordCountDictList):
        '''
            description: input an new file then update the all word list
            input:
                newWordCountDict: new input string word count dict
            output:
                self.all_word_dict
        '''
        n = len(newWordCountDictList)
        all_word_list = []
        all_word_dict = {}
        for i in range(0,n):
            all_word_list = list(set(all_word_list + newWordCountDictList[i].keys()))
        for i in range(0,len(all_word_list)):
            all_word_dict[all_word_list[i]]=0
        return all_word_dict
#-----------------********************-----------------#
    def constructFeatureDict(self, newWordCountDict, all_word_dict):
        '''
            description: construct feature dict for the new input string
            input:
                newWordCountDict: word count dict of the new input string
            output:
                sample_feature_dict: feature dict for new input string
        '''
        sample_feature_dict = {}
        for key in all_word_dict.keys():
            sample_feature_dict[key] = all_word_dict[key]
        for key in newWordCountDict.keys():
            sample_feature_dict[key] = newWordCountDict[key]
        return sample_feature_dict


#-----------------********************-----------------#


if __name__ == "__main__":
    wordseg = wordSeg()
    sc = SparkContext(appName="wordSegTest")
    lines = sc.textFile("hdfs://warrior:9000/testData/newsfile/new02")
    readWordCountDict = lines.map(lambda s:wordseg.GetWordCountTable(s))
    readWordCountDict.saveAsTextFile("hdfs://warrior:9000/testData/splitTestResult")
    status, results = commands.getstatusoutput("hadoop fs -cat hdfs://warrior:9000/testData/splitTestResult/part-00000")
    print results
    status, results = commands.getstatusoutput("hadoop fs -rmr hdfs://warrior:9000/testData/splitTestResult")
    print results
    #readWordCountDict.collect()
    print "hello!!"
    sc.stop()
