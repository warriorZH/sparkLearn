#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: clusterAlgorithm.py
#description: cluster algorithm for news use
#             use  K-Means for whole
#                   pearson for correlation
#                   DB_index for select optimize "k"
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-3-17
#log:


import math
#********************-----------------********************#

#********************-----------------********************#
class clusterAlgorithm(object):
    '''
        K-Means cluster algorithm for text
    '''
    def __init__(self):
        self.cluster_class_sample_record=[]
        self.cluster_class_centre=[]
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
        # print correlation_value
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
        correlation_value = (n_sum_Xi_Yi-sum_Xi*sum_Yi) / math.sqrt( (n_sum_Xi2-sum2_Xi) * (n_sum_Yi2-sum2_Yi) )
        return (correlation_value+1)/2


#-----------------********************-----------------#
    def once_K_MeansCluster(self, corr_fun, sample, k_class_centre, k):
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


#-----------------********************-----------------#
    def K_MeansCluster(self, corr_fun, samples, k, theta=50, num=20):
        '''
            description: execute K-Means cluster mannage
            input:
                corr_fun: method of calculate correlation
                samples: samples[{}] dict list
                k: k class
                theta: restrain limit value
                num : fixed iteration times
            output:
                none
        '''
        iterator_count_number = 0
        #属于相应类别的样本记录
        k_class_sample_record = [[]for i in range(0,k)]
        #每次迭代的相关系数记录
        calcu_correlation_value_list = range(0,k)
        #初始化一个含有多个字典的列表，用于存储k个类中心
        k_class_centre = [{}for i in range(0,k)]
        pre_k_class_centre = [{}for i in range(0,k)]
        circul_limit_theta = 0
        #初始化k个类中心
        k_class_centre = samples[0:k]
        # for i in range(0,k):
        #     for key in samples[i].keys():
        #         k_class_centre[i][key] = samples[i][key]
        if len(samples)>k:
            #开始迭代计算
            for iterator_num in range(0, num):
                iterator_count_number += 1
                #一次迭代
                #存储上一次的类中心，用于计算两次迭代间类中心值的变化
                for i in range(0,k):
                    for key in k_class_centre[i].keys():
                        pre_k_class_centre[i][key] = k_class_centre[i][key]
                #reset k_class_sample_record
                k_class_sample_record = [[]for i in range(0,k)]
                #进行一次聚类操作
                for sample_index in range(0, len(samples)):
                    for i in range(0,k):
                        #计算相关系数 0-1与相关成正比
                        calcu_correlation_value_list[i] = corr_fun(k_class_centre[i],samples[sample_index])
                    #计算与sample_index这个样本对应的最相关的那个类，
                    max_corr = max(calcu_correlation_value_list)
                    #相关性最大的类的索引
                    max_corr_index = calcu_correlation_value_list.index(max_corr)
                    #然后将sample_index加入到类的记录中
                    k_class_sample_record[max_corr_index].append(sample_index)
                #print k_class_sample_record
                #重新计算类中心
                for i in range(0,k):
                    #reset k_class_sum
                    k_class_sum = {}
                    for dict_key in k_class_centre[i].keys():
                        k_class_sum[dict_key] = 0
                    for k_sample_index in k_class_sample_record[i]:
                        for dict_key in k_class_centre[i].keys():
                            k_class_sum[dict_key] += samples[k_sample_index][dict_key]
                    # print k_class_sample_record
                    for dict_key in k_class_centre[i].keys():
                        if(len(k_class_sample_record[i])>0):
                            k_class_centre[i][dict_key] = k_class_sum[dict_key]/(len(k_class_sample_record[i]))
                        else:
                            print str(i)+"class has no element!"

                #计算是不是达到收敛极限
                circul_limit_theta = 0
                for i in range(0,k):
                    for centre_dict_key in k_class_centre[0].keys():
                        circul_limit_theta += abs(k_class_centre[i][centre_dict_key]-pre_k_class_centre[i][centre_dict_key])
                if(circul_limit_theta<theta):
                    print "the last theta: "+str(circul_limit_theta)
                    print "#####################"
                    break
            print "iterator count number: "+str(iterator_count_number)
            print "k number: "+str(k)
            #记录各个类中元素和类中心
            self.cluster_class_sample_record = [[] for i in range(0,k)]
            self.cluster_class_centre = [{} for i in range(0,k)]
            for class_index in range(0,k):
                self.cluster_class_centre[class_index] = k_class_centre[class_index]
                self.cluster_class_sample_record[class_index] = k_class_sample_record[class_index]
        else:
            print "error k value!!"
