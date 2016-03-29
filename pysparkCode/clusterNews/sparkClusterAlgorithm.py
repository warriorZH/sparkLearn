#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: sparkClusterAlgorithm.py
#description: in spark platform
#             cluster algorithm for news
#             use  K-Means for whole
#                   pearson for correlation
#                   DB_index for select optimize "k"
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-17
#log:


import math
#********************-----------------********************#

#********************-----------------********************#
class sparkClusterAlgorithm(object):
    '''
        K-Means cluster algorithm for text
    '''
    def __init__(self):
        pass
        # self.cluster_class_sample_record=[]
        # self.cluster_class_centre=[]



#-----------------********************-----------------#
    def calcu_distance_corr(self, sample_feature_dict_A, sample_feature_dict_B):
        '''
            description: calculate distance correlation of text_A and text_B

                                          1
                P = --------------------------------------------------------
                                1 +  squr([sum((Xi-Yi)2)])

            input:
                sample_feature_dict_A: word dict of text_A
                sample_feature_dict_B: word dict of text_B
            output:
                cosine_correlation_value
        '''
        n = len(sample_feature_dict_A)
        m = len(sample_feature_dict_B)
        if n>m:
            n=m
        sample_feature_list_A = sample_feature_dict_A.values()
        sample_feature_list_B = sample_feature_dict_B.values()
        sum_Xi_Yi_2 = 0
        for i in range(0,n):
            sum_Xi_Yi_2 += (sample_feature_list_A[i]-sample_feature_list_B[i])*(sample_feature_list_A[i]-sample_feature_list_B[i])
        correlation_value = 1/(1 + math.sqrt(sum_Xi_Yi_2))
        return correlation_value


#-----------------********************-----------------#
    def calcu_cosine_corr(self, sample_feature_dict_A, sample_feature_dict_B):
        '''
            description: calculate cosine correlation of text_A and text_B

                                          sum(Xi*Yi)
                P = --------------------------------------------------------
                                  squr([sum(Xi2)*sum(Yi2)])

            input:
                sample_feature_dict_A: word dict of text_A
                sample_feature_dict_B: word dict of text_B
            output:
                cosine_correlation_value
        '''
        n = len(sample_feature_dict_A)
        m = len(sample_feature_dict_B)
        if n>m:
            print "correlation dict length error"
            n=m
        sample_feature_list_A = sample_feature_dict_A.values()
        sample_feature_list_B = sample_feature_dict_B.values()
        sum_Xi_Yi = 0
        for i in range(0,n):
            sum_Xi_Yi += sample_feature_list_A[i]*sample_feature_list_B[i]
        sum_Xi2 = 0
        for i in range(0,n):
            sum_Xi2 += sample_feature_list_A[i]*sample_feature_list_A[i]
        sum_Yi2 = 0
        for i in range(0,n):
            sum_Yi2 += sample_feature_list_B[i]*sample_feature_list_B[i]
        correlation_value = sum_Xi_Yi/math.sqrt(sum_Xi2*sum_Yi2)
        return correlation_value



#-----------------********************-----------------#
    def calcu_pearson_corr(self, sample_feature_dict_A, sample_feature_dict_B):
        '''
            description: calculate pearson correlation of text_A and text_B

                              n*sum(Xi*Yi) - sum(Xi)*sum(Yi)
                P = --------------------------------------------------------
                     squr([n*sum(Xi2) - sum(Xi)2]*[n*sum(Yi2) - sum(Yi)2])

            input:
                sample_feature_dict_A: word dict of text_A
                sample_feature_dict_B: word dict of text_B
            output:
                pearson_correlation_value
        '''
        n = len(sample_feature_dict_A)
        m = len(sample_feature_dict_B)
        if n>m:
            n=m
        sample_feature_list_A = sample_feature_dict_A.values()
        sample_feature_list_B = sample_feature_dict_B.values()
        n_sum_Xi_Yi = 0
        for i in range(0,n):
            n_sum_Xi_Yi += sample_feature_list_A[i]*sample_feature_list_B[i]
        n_sum_Xi_Yi = n_sum_Xi_Yi*n
        sum_Xi = sum(sample_feature_list_A)
        sum2_Xi = sum_Xi*sum_Xi
        sum_Yi = sum(sample_feature_list_B)
        sum2_Yi = sum_Yi*sum_Yi
        n_sum_Xi2 = 0
        for i in range(0,n):
            n_sum_Xi2 += sample_feature_list_A[i]*sample_feature_list_A[i]
        n_sum_Xi2 = n_sum_Xi2*n
        n_sum_Yi2 = 0
        for i in range(0,n):
            n_sum_Yi2 += sample_feature_list_B[i]*sample_feature_list_B[i]
        n_sum_Yi2 = n_sum_Yi2*n
        print math.sqrt( abs((n_sum_Xi2-sum2_Xi) * (n_sum_Yi2-sum2_Yi)) )
        correlation_value = (n_sum_Xi_Yi-sum_Xi*sum_Yi) / math.sqrt( (n_sum_Xi2-sum2_Xi) * (n_sum_Yi2-sum2_Yi) )
        return (correlation_value+1)/2  #abs(correlation_value)#


#-----------------********************-----------------#
    def K_MeansCluster(self, corr_fun, sample, k_class_centre, k):
        '''
            description: execute K-Means cluster mannage
            input:
                corr_fun: method of calculate correlation
                sample: sample dict
                k: number of  class
                k_class_centre:
            output:
                max_corr_index
        '''
        #每次迭代的相关系数记录
        calcu_correlation_value_list = range(0,k)
        for i in range(0,k):
            #计算相关系数 0-1与相关成正比
            calcu_correlation_value_list[i] = corr_fun(k_class_centre[i],sample)
        #计算与sample_index这个样本对应的最相关的那个类，
        max_corr = max(calcu_correlation_value_list)
        #相关性最大的类的坐标
        print calcu_correlation_value_list
        max_corr_index = calcu_correlation_value_list.index(max_corr)
        return max_corr_index
