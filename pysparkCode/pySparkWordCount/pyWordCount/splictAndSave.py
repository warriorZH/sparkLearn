#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: splictAndSave.py
#description: an python in spark test splict and save as txt file in hdfs
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-1
#log:


from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext(appName="splictAndSave")
    files = sc.textFile("hdfs://warrior:9000/testData/CHANGES.txt")
    words = files.flatMap(lambda x: x.split(' '))
    words.cache()
    words.saveAsTextFile("hdfs://warrior:9000/testData/splictTestResult/wordresult")
    counts = words.map(lambda x: (x, 1)) \
                  .reduceByKey(lambda a,b: a+b)
    counts.saveAsTextFile("hdfs://warrior:9000/testData/splictTestResult/countresult")
    #output = counts.collect()
    #for (word, count) in output:
    #    print "%s:%i" % word, count
    sc.stop()
