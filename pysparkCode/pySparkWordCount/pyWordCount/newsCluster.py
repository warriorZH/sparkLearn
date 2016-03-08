#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: newsCluster.py
#description: cluster news files in spark platform
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-3
#log:

from pyspark import SparkContext

if __name__ == "__main__" :
    sc = SparkContext(appName="newsCluster")

    filesPool = sc.wholeTextFiles("hdfs://warrior:9000/testData/newsfile", use_unicode=False)

    print "keys: %s \n" % filesPool.values()
    sc.stop()
