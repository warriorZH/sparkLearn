#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: __init__.py
#description: test code
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-5
#log:

#wordfilepath = "/home/warrior/gitDir/PythonCode/MyParticiple/dataSource/gold/pku_training_words.utf8"
#wordfile = open(wordfilepath, 'r')
#try:
#    all_word_lines = wordfile.read()
#except:
#    print "open file error!!"
#finally:
#    wordfile.close()

#wordList = all_word_lines.split('\n')
#wordList = sorted(wordList)
#for i in range(5000,9000):
#    print("%d: %s\n" % (i, wordList[i]))

import re
import numpy

#wordelem = [[],[],[]]
#wordelem[0] = "办公2"
#wordelem[1] = "办公"
#wordelem[2] = "全世界人民张开双臂，迎接人类历史的又一个新纪元"
#wordTemp = ""
#wordlist = wordelem[2]
## = re.compile('''(?:[0-\x79]{1}?|[\x80-\xff]{3}?)''')
#list(wordelem3)
#wordlist = p.findall(wordelem[2])
#print wordlist
#print list("今天天气真好")
#print len(wordlist)
#if wordlist[1] == '天':
#    print "greate!!"
#else:
#    print "oh NO!!"
#print len(wordelem[0])

#for i in range(0,3):
#    wordTemp = wordTemp+wordlist[i]
#print wordTemp
#print len(wordelem[2])

#if wordelem[0] in wordelem[1]:
#    print "haha"
#else:
#    print "wuwu"
#a = int((3+8)/2)
#print a

#dictTest = {}
#dictTest[1] = 5
#dictTest[2] = 9
#dictTest[3] = 315
#dictTest[4] = 7
#dictTest[5] = 315
#valueTemp = dictTest.values()
#valueTemp.sort(reverse=True)
#listTemp = []
#print len(listTemp)
#listTemp = sorted(dictTest.items(), key=lambda d: d[1], reverse=True)
#print listTemp[1][0]
#print listTemp

#list2 = [[] for i in range(0,13)]

#list2[0].append("haha")
#list2[0].append("lplp")
#list2[1].append("lulu")
#list2[1].append("sasa")
#list2[2].append("koko")
#list3 = list2
#print list3
#print len(list3)

#print valueTemp



#numlist = [1,2,3]
#varRecord = numpy.var(numlist)
#print varRecord


#storageResultpath = "/home/warrior/gitDir/PythonCode/MyParticiple/codeSource/my_pku_test_gold.utf8"
#fd = open(storageResultpath,'r')
#linedata = fd.readline()
#while(linedata):
#    print linedata
#    linedata = fd.readline()
#fd.close()


#from MMSEG import *
#wordfilepath = "/home/warrior/gitDir/PythonCode/MyParticiple/dataSource/gold/pku_training_words.utf8"
#wordCountPath = "/home/warrior/gitDir/PythonCode/MyParticiple/codeSource/staticalResult.utf8"

#wordelem2 = "今天天真好"
#mmseg = MMSEG()
#mmseg.getwordsDict(wordfilepath)
#mmseg.getWordCountDict(wordCountPath)
#mmseg.MMSEGStep1MaxThreeLength(wordelem2, mmseg.wordList)
#for element in mmseg.sentencePartWordList:
#    print element

alist = [1,2,3]
blist = [4,5,6]
clist = alist + blist
print clist

crfSourceStr = "在  20  啦啦啦 世纪  里  ， "
rPattern = re.compile('''[\s]{1,}''')
midList = rPattern.split(crfSourceStr)
rePatternTag = re.compile('''(?:[0-\x79]+|[\x80-\xff]{3}?)''')

wordTagList = []
wordTagCURList = []
for item in midList:
    #print item
    itemList = rePatternTag.findall(item)
    if(len(itemList)>1):
        wordTagCURList.append(itemList[0])
        wordTagCURList.append("B")
        wordTagList.append(wordTagCURList)
        wordTagCURList = []
        for wordIndex in range(1,len(itemList)-1):
            wordTagCURList.append(itemList[wordIndex])
            wordTagCURList.append("M")
            wordTagList.append(wordTagCURList)
            wordTagCURList = []
        wordTagCURList.append(itemList[len(itemList)-1])
        wordTagCURList.append("E")
        wordTagList.append(wordTagCURList)
        wordTagCURList = []
    else:
        if(itemList):
            #print itemList
            wordTagCURList.append(itemList[0])
            wordTagCURList.append("S")
            wordTagList.append(wordTagCURList)
            wordTagCURList = []
print "%d" % len(wordTagList)
for item in range(0,len(wordTagList)):
    #for subItem in wordTagList[item]:
    print wordTagList[item][0]+"   "+wordTagList[item][1]+"\n"
    #print str(item)+"\n"
print wordTagList



#testDict = {"aa":1, "bb":2, "cc":3}
#print testDict["aa"]
#print testDict.has_key("bb")
#print testDict.has_key("dd")
