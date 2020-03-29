# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:30:20 2020

@author: FreeA7

https://www.nowcoder.com/practice/df2ebc45eab84099b843f0bfd8989516

给定n个数字的序列a，对位置i进行一次操作将使得a_{i-1},a_i,a_{i+1}a，都变成max(a_{i-1},a_i,a_{i+1})
并且操作过位置i之后，位置0到i都不能再操作

设最多可以操作k(k≤n)次，最后得到的整个序列的总和最大可以是m_k你需要求出m_1,m_2,...m_n 

示例
输入:
    5,[1,2,3,4,5]
输出:
    [18,21,22,22,22]
说明：
    输入：
        n=5, 输入序列为[1,2,3,4,5]
        
        [1,2,3,4,5]对应位置0,1,2,3,4
        只能操作1次的时候，对位置1操作得到[3,3,3,4,5]
        或者对位置2操作可以得到[1,4,4,4,5]
        或者对位置3操作可以得到[1,2,5,5,5]，都可以得m_1=18m 

        只能操作2次的时候，按次序操作位置1和位置3可以得到[3,3,5,5,5]，其他操作不会得到更优的结果，所以m_2=21m 

        能操作3次以上的时候可以得到的最优序列为[3,4,5,5,5]（依次操作位置1，位置2，位置3）,所以m_3=22,m_4=22,m_5=22m 
"""

# 单步最优，错误
from utils import timer
import random


class Solution1:
    def getMax(self, li, i):
        if i == 0:
            max_i = max([li[0], li[1]])
            li[0] = max_i
            li[1] = max_i
        elif i == len(li)-1:
            max_i = max([li[i], li[i]-1])
            li[i] = max_i
            li[i-1] = max_i
        else:
            max_i = max([li[i-1], li[i], li[i+1]])
            li[i] = max_i
            li[i-1] = max_i
            li[i+1] = max_i
        return li
        
    @timer
    def solve(self , n , a ):
        k = n
        li = a
        list_dict = [{'list':li.copy(), 'sum':sum(li), 'sum_list':[sum(li)], 'index_list':[0]}]
        
        while k:
            k = k-1
            list_dict_this_k = []
            for record_i in range(len(list_dict)):
                max_this = list_dict[-1]['sum']
                list_dict_this_re = []
                for i in range(list_dict[record_i]['index_list'][-1], len(a)):
                    li = list_dict[record_i]['list'].copy()
                    li = self.getMax(li, i)
                    sum_li = sum(li)
                    if sum_li >= max_this:
                        list_dict_this_re.append({'list':li.copy(), 'sum':sum_li, 
                                               'sum_list':list_dict[record_i]['sum_list'] + [sum_li], 
                                               'index_list':list_dict[record_i]['index_list'] + [i]})
                        max_this = sum_li
                list_dict_this_re_temp = []
                for i in range(len(list_dict_this_re)):
                    if list_dict_this_re[i]['sum'] == max_this:
                        list_dict_this_re_temp.append(list_dict_this_re[i])
                list_dict_this_k.append(list_dict_this_re_temp)
            max_k = max([i[-1]['sum'] for i in list_dict_this_k])
            list_dict = []
            for i in range(len(list_dict_this_k)):
                if list_dict_this_k[i][-1]['sum'] == max_k:
                    list_dict += list_dict_this_k[i]
        
        return list_dict[-1]['sum_list'][1:]
    
    
# 遍历，正确
class Solution2:
    def getMax(self, li, i):
        if i == 0:
            max_i = max([li[0], li[1]])
            li[0] = max_i
            li[1] = max_i
        elif i == len(li)-1:
            max_i = max([li[i], li[i]-1])
            li[i] = max_i
            li[i-1] = max_i
        else:
            max_i = max([li[i-1], li[i], li[i+1]])
            li[i] = max_i
            li[i-1] = max_i
            li[i+1] = max_i
        return li
        
    def everyK(self , n , a ):
        k = n
        li = a
        list_dict = [{'list':li.copy(), 'sum':sum(li), 'sum_list':[sum(li)], 'index_list':[0]}]
        
        while k:
            k = k-1
            list_dict_this_k = []
            for record_i in range(len(list_dict)):
                list_dict_this_re = []
                for i in range(list_dict[record_i]['index_list'][-1], len(a)):
                    li = list_dict[record_i]['list'].copy()
                    li = self.getMax(li, i)
                    sum_li = sum(li)
                    list_dict_this_re.append({'list':li.copy(), 'sum':sum_li, 
                                           'sum_list':list_dict[record_i]['sum_list'] + [sum_li], 
                                           'index_list':list_dict[record_i]['index_list'] + [i]})
                list_dict_this_k.append(list_dict_this_re)
            list_dict = []
            for i in range(len(list_dict_this_k)):
                list_dict += list_dict_this_k[i]
        
        max_end = max([i['sum'] for i in list_dict])
        print(len(list_dict))
        for i in list_dict:
            if i['sum'] == max_end:
                return i['sum_list'][-1]
            
    @timer
    def solve(self , n , a ):
        return [self.everyK(i,a) for i in range(1,n+1)]
 
    
# 遍历，正确，排除首位以及重复
class Solution3:
    def getMax(self, li, i):
        if i == 0:
            max_i = max([li[0], li[1]])
            li[0] = max_i
            li[1] = max_i
        elif i == len(li)-1:
            max_i = max([li[i], li[i]-1])
            li[i] = max_i
            li[i-1] = max_i
        else:
            max_i = max([li[i-1], li[i], li[i+1]])
            li[i] = max_i
            li[i-1] = max_i
            li[i+1] = max_i
        return li
        
    def everyK(self , n , a ):
        k = n
        li = a
        list_dict = [{'list':li.copy(), 'sum':sum(li), 'sum_list':[sum(li)], 'index_list':[0]}]
        
        while k:
            k = k-1
            list_dict_this_k = []
            for record_i in range(len(list_dict)):
                list_dict_this_re = []
                for i in range(list_dict[record_i]['index_list'][-1]+1, len(a)-1):
                    li = list_dict[record_i]['list'].copy()
                    li = self.getMax(li, i)
                    sum_li = sum(li)
                    list_dict_this_re.append({'list':li.copy(), 'sum':sum_li, 
                                           'sum_list':list_dict[record_i]['sum_list'] + [sum_li], 
                                           'index_list':list_dict[record_i]['index_list'] + [i]})
                if list_dict_this_re != []:
                    list_dict_this_k.append(list_dict_this_re)
            if list_dict_this_k != []:
                list_dict = []
                for i in range(len(list_dict_this_k)):
                    list_dict += list_dict_this_k[i]
        
        
        max_end = max([i['sum'] for i in list_dict])
#        print(len(list_dict))
        for i in list_dict:
            if i['sum'] == max_end:
                return i['sum_list'][-1]
            
    @timer
    def solve(self , n , a ):
        return [self.everyK(i,a) for i in range(1,n+1)]
    
    
# Bitmasking + DP
class Solution4:
    @timer
    def solve(self , n , a ):
        dp = [[0 for mask in range(2**len(a))] for k in range(n+1)]
        sum_origin = sum(a)
        dp[0] = [sum_origin for mask in range(2**len(a))]
        if not n or len(a) == 1:
            return dp[0][0]
        if len(a) == 2:
            return 2*max(a)
        for mask in range(2**len(a)):
            if mask&1 or mask&(1<<(len(a)-1)):
                continue
            k = 0
            for i in bin(mask)[2:]:
                if i=='1': k+=1
            if k>=n:
                continue
            temp_a = a.copy()
            for i in range(len(temp_a)):
                if mask&(1<<i):
                    max_temp = max(temp_a[i-1], temp_a[i], temp_a[i+1])
                    temp_a[i-1], temp_a[i], temp_a[i+1] = max_temp, max_temp, max_temp
            for i in range((len(bin(mask))-2), len(temp_a)-1):
                max_temp = max(temp_a[i-1], temp_a[i], temp_a[i+1])
                plus = 3*max_temp - sum([temp_a[i-1], temp_a[i], temp_a[i+1]])
                dp[k+1][mask|1<<i] = max(dp[k+1][mask|1<<i], dp[k][mask]+plus)
        output = []
        for i in range(1,n+1):
            max_temp = max(dp[i])
            if max_temp:
                output.append(max(dp[i]))
            else:
                output.append(output[-1])
        return output


# 错误的动态规划，因为这个的transition是dp[k] = max(dp[k-1]+f(1), dp[k-1]+f(2) ... dp[k-1]+f(n))
# 但是在这道题这里这是错误的，比如01背包问题，拿商品的顺序是无所谓的，放不放入唯一影响的的背包剩余空间，所以用背包剩余空间来确定状态就可以
# 所以01背包需要用背包剩余空间和还要判断的商品数量来进行dp，dp的值是商品价值
# 这道题问题在于，每次采取的措施虽然是无序的，但只要知道了都在那些位子上进行过操作，从小向大推导即可得出当前a
# 但是dp的状态必须要包含两点：
#        1.进行操作的轮数 k
#        2.之前轮数进行的操作都是什么 => 当然如果知道每一轮的操作也就不需要k了，因为操作数就是轮数
#        （dp不仅仅只取决于轮数，还取决于之前的操作，因此不同的操作都会导致不同的数列a，这就像是01背包中的我们的背包状态）
# 而dp的值是数列之和，所以这种错误的做法只考虑了轮数，没有考虑背包状态，就像01背包只考虑了拿一个一个商品没有考虑剩余空间
# 所以用bitmasking进行举例的话就是transition应该是dp[k+1][mask|1<<i] = max(dp[k+1][mask|1<<i], dp[k][mask]+f(mask,i))，遍历每一个i
# 因为dp的变化值f()必须要之前轮数的操作和当前要进行的操作才能算出来
class Solution5:
    @timer
    def solve(self , n , a ):
        dp = [0 for _ in range(n+1)]
        dp[0] = sum(a)
        max_dict = [{'index':0, 'list':a.copy()}]
        for k in range(1, len(a)+1):
            max_k_dict = []
            for record in max_dict:
                for i in range(record['index']+1, len(a)-1):
                    max_temp = max(record['list'][i-1], record['list'][i], record['list'][i+1])
                    plus = 3*max_temp - sum([record['list'][i-1], record['list'][i], record['list'][i+1]])
                    if dp[k-1]+plus > dp[k]:
                        dp[k] = dp[k-1]+plus
                        temp_list = record['list'].copy()
                        temp_list[i-1], temp_list[i], temp_list[i+1] = max_temp, max_temp, max_temp
                        temp_max_dict = [{'index':i, 'list':temp_list.copy()}]
                    elif dp[k-1]+plus == dp[k] and plus!=0:
                        temp_list = record['list'].copy()
                        temp_list[i-1], temp_list[i], temp_list[i+1] = max_temp, max_temp, max_temp
                        temp_max_dict.append({'index':i, 'list':temp_list.copy()})
                for dic in temp_max_dict:
                    if dic not in max_k_dict:max_k_dict.append(dic)
            max_dict = max_k_dict
        return dp[1:]
    

# DP，重点在于用最少的变量
class Solution6:
    @timer
    def solve(self , n , a ):
        max_v = max(a)
        sum_a = sum(a)
        # 进行了k次操作，考虑前i个数，在不考虑i+1情况下，a[i]变为v整个序列最多增加了多少，01表示第i个数字进行操作与否
        dp = [[[[0, 0] for v in range(max_v+1)] for i in range(len(a))] for k in range(n+1)]
        for i in range(len(a)-1):
            for k in range(i+1):
                for v in range(a[i], max_v+1):
                    # 00 i和i+1都没有进行操作
                    dp[k][i+1][a[i+1]][0] = max(dp[k][i+1][a[i+1]][0], dp[k][i][v][0])
                    # 10 i进行了操作
                    if v > a[i+1]:
                        dp[k][i+1][v][0] = max(dp[k][i+1][v][0], dp[k][i][v][1]+(v-a[i+1]))
                    else:
                        dp[k][i+1][a[i+1]][0] = max(dp[k][i+1][a[i+1]][0], dp[k][i][v][1]+(a[i+1]-v))
                    # 01 i+1进行了操作
                    if v > a[i+1]:
                        dp[k+1][i+1][v][1] = max(dp[k+1][i+1][v][1], dp[k][i][v][0]+(v-a[i+1]))
                    else:
                        dp[k+1][i+1][a[i+1]][1] = max(dp[k+1][i+1][a[i+1]][1], dp[k][i][v][0]+(a[i+1]-v))
                    # 11 i和i+1都进行了操作
                    if v > a[i+1]:
                        dp[k+1][i+1][v][1] = max(dp[k+1][i+1][v][1], dp[k][i][v][1]+(v-a[i+1]))
                    else:
                        dp[k+1][i+1][a[i+1]][1] = max(dp[k+1][i+1][a[i+1]][1], dp[k][i][v][1]+(a[i+1]-v))      
        max_sum = 0
        for k in range(1,n+1):
            for i in range(len(a)):
                for v in range(max_v+1):
                    print(dp[k][i][v]+[max_sum])
                    max_sum = max(dp[k][i][v]+[max_sum])
            a[k-1] = max_sum + sum_a
        print(a)
                
                  
    
# --------------------- 输出 ---------------------
target1 = [5,[1,2,3,4,5]]
target2 = [10, [1 for i in range(10)]]
target3 = [20, [1 for i in range(20)]]
target4 = [10,[163,65,106,146,82,28,162,92,196,143]]

tar = target1

s = Solution1()
print(s.solve(tar[0], tar[1]))

s = Solution2()
print(s.solve(tar[0], tar[1]))

s = Solution3()
print(s.solve(tar[0], tar[1]))

s = Solution4()
print(s.solve(tar[0], tar[1]))

s = Solution6()
print(s.solve(tar[0], tar[1]))
    
            
'''
Solution1.solve 共用时：1.1689544000000751 s
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
10
55
220
715
2002
5005
11440
24310
48620
92378
Solution2.solve 共用时：6.135507200000575 s
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
8
28
56
70
56
28
8
1
1
1
Solution3.solve 共用时：0.013734600001043873 s
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
Solution4.solve 共用时：0.003085199998167809 s
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
'''
                    
                