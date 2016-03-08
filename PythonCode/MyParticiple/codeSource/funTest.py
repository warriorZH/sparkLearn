#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: __init__.py
#description: test code
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-5
#log:

from MMSEG import *

lineCounter = 0
wordfilepath = "/home/warrior/gitDir/PythonCode/MyParticiple/dataSource/gold/pku_training_words.utf8"
storageResultpath = "/home/warrior/gitDir/PythonCode/MyParticiple/my_pku_test_gold.utf8"
getPartDatapath = "/home/warrior/gitDir/PythonCode/MyParticiple/dataSource/testing/pku_test.utf8"
getDataFile = open(getPartDatapath, 'r')
storDataFile = open(storageResultpath, 'w')
mmseg = MMSEG()
mmseg.getwordsDict(wordfilepath)

wordelem2 = getDataFile.readline()
mmseg.MMSEGStep1MaxThreeLength(wordelem2, mmseg.wordList)
while(wordelem2):
    for i in mmseg.sentencePartWordList:
        storDataFile.write(i+"  ")
    storDataFile.write("\n")
    wordelem2 = getDataFile.readline()
    mmseg.MMSEGStep1MaxThreeLength(wordelem2, mmseg.wordList)
    lineCounter+=1
    print "manage %d lines" % lineCounter
storDataFile.close()
getDataFile.close()
