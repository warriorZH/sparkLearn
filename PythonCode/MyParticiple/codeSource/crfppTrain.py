#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: __init__.py
#description: use crf++ algorithm tool to optimize the mmseg result
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-8
#log:


import re
import commands

#********************-----------------********************#

#********************-----------------********************#
class crfppTrain(object):
    '''
        use use crf++ algorithm tool to optimize the mmseg result, this class is for training model
        tool get:https://drive.google.com/folderview?id=0B4y35FiV1wh7fngteFhHQUN2Y1B5eUJBNHZUemJYQV9VWlBUb3JlX0xBdWVZTWtSbVBneU0&usp=drive_web#list
    '''
    def __init__(self):
        pass


    #-----------------********************-----------------#
    def getTrainData(self, sourceDataPath,crfppTrainPath):
        '''
            description: get train data from sourceDataPath, and output the crf++ specified form data in crfTrainData.utf8
            input:
                sourceDataPath: the train source data file path
                crfppTrainPath: the train result data file path
            output:
                none
        '''
        onlineSourceData = ""
        onelineTrainData = ""
        midList = []
        wordTagList = []
        wordTagCURList = []
        itemList = []

        sourceDataFile = open(sourceDataPath,'r')
        crfTrainDataFile = open(crfppTrainPath,'w')
        onlineSourceData = sourceDataFile.readline()
        while(onlineSourceData):
            rPattern = re.compile('''[\s]{1,}''')
            midList = rPattern.split(onlineSourceData)
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
                        wordTagCURList.append(itemList[0])
                        wordTagCURList.append("S")
                        wordTagList.append(wordTagCURList)
                        wordTagCURList = []
            for item in range(0,len(wordTagList)):
                onelineTrainData = wordTagList[item][0]+"     "+wordTagList[item][1]+"\n"
                crfTrainDataFile.write(onelineTrainData)
            crfTrainDataFile.write("\n") #以换行来标记一行的结束
            onlineSourceData = sourceDataFile.readline()
        crfTrainDataFile.close()
        sourceDataFile.close()

    #-----------------********************-----------------#
    def excuteCRFTrain(self, templatePath, trainDataPath, modelName="cfr_model"):
        '''
            description: excute train action and create model
            input:
                none
            output:
                none
        '''

        resultStatue = ""
        resultOutput = ""
        command = "crf_learn -f 3 -c 1.5 "+templatePath+" "+trainDataPath+" "+modelName
        resultStatue,resultOutput = commands.getstatusoutput(command)
        print resultOutput


sourcePath = "/home/warrior/gitDir/PythonCode/MyParticiple/dataSource/training/pku_training.utf8"
resultpath = "/home/warrior/gitDir/PythonCode/MyParticiple/crfMidFiles/train_form_result.utf8"
templatePath = "/home/warrior/gitDir/PythonCode/MyParticiple/codeSource/template"
crftrain = crfppTrain()
#crftrain.getTrainData(sourcePath,resultpath)
#print "get traing data complete!!"
print "start training!!"
crftrain.excuteCRFTrain(templatePath, resultpath, "crf_model")
print "training complete!!"
