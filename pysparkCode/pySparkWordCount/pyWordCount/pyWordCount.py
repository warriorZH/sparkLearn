#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: pyWordCount.py
#description: an python in spark test word count
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-2-29
#log:


from pyspark import SparkContext
import commands




sc = SparkContext(appName="pyWordCount")
lines = sc.textFile("hdfs://warrior:9000/testData/newsfile/new02")
lineLengths = lines.map(lambda s: len(s))
print lineLengths
lineLengths.persist()
totalLength = lineLengths.reduce(lambda a,b: a+b)
lineLengths.saveAsTextFile("hdfs://warrior:9000/testData/wcTestResult")
print "file total line: %d" % totalLength
status, results = commands.getstatusoutput("hadoop fs -cat hdfs://warrior:9000/testData/wcTestResult/part-00000")
print results
status, results = commands.getstatusoutput("hadoop fs -rmr hdfs://warrior:9000/testData/wcTestResult")
print results
sc.stop()
