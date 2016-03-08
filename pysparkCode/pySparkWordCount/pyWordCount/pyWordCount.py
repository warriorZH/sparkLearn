#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: pyWordCount.py
#description: an python in spark test word count
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-2-29
#log:


from pyspark import SparkContext




sc = SparkContext(appName="pyWordCount")
lines = sc.textFile("hdfs://warrior:9000/testData/CHANGES.txt")
lineLengths = lines.map(lambda s: len(s))
lineLengths.persist()
totalLength = lineLengths.reduce(lambda a,b: a+b)
lineLengths.saveAsTextFile("hdfs://warrior:9000/testData/wcTestResult")
print "file total line: %d" % totalLength
sc.stop()
