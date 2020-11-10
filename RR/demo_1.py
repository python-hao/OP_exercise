# pcb_list=[0,5,9,8,41,55,3]
# pcb_list.sort(key=lambda x:x,reverse=True)
# over_list =pcb_list.copy()
# for i in pcb_list[::-1]:
#     if i <= 8:
#         a = pcb_list.pop(-1)
#         print(a)
#
# print(over_list,pcb_list)
# print(pcb_list[-1])
# selfpcb_queue =[0,5,6,9,8,4]
# selfpcb_queue.append(3)
# pcb_list.pop(-1)
# print(selfpcb_queue,pcb_list)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： XHao
# datetime： 2020/11/2 21:57
# ide： PyCharm
import random
import time
from functools import reduce

class Pcb:
    def __init__(self):
        self.name = ""  # 作业名字
        self.arrivetime = float(random.randint(1, 15))  # 到达时间
        self.runtime = float(random.randint(1, 10))  # 服务时间
        self.finishtime = 0  # 完成时间
        self.zztime = 0  # 周转时间
        self.weightzztime = 0  # 带权周转时间
        self.finished = False  # 进程标志，是否已经执行完了
        self.temp = 0           # 用于记录pcb经历 temp 次时间片(计算服务时间、这个变量是最后添加的）

class RR:
    def __init__(self):
        self.pcb_num = int(input("请输进程数量："))
        self.pcb_list = []
        self.pcb_queue = []
        for i in range(self.pcb_num):
            pcb = Pcb()
            pcb.name = str(input("麻烦老哥输入第{}个pcb的名字：".format(i + 1)))
            self.pcb_list.append(pcb)
        print("~~~~~进程信息~~~~~：")
        self.output_rr(self.pcb_list)
        self.rr()

    def rr(self):
        self.time_chip = float(input("请输入时间片大小："))
        self.pcb_list.sort(key=lambda x: x.arrivetime, reverse=True)  # pcb列表元素按到达时间排个队,从大到小
        self.over_list = []                             # 已经结束的pcb集合
        self.pcb_queue.append(self.pcb_list[-1])        # 就绪队列初始化
        self.pcb_list.pop(-1)
        # self.output_rr(self.pcb_list)   #测试
        # self.ppp = input("asd:")    #测试
        self.starttime = self.pcb_queue[0].arrivetime   # 第一个pcb的开始时间

        while(True):
            pcb2 = self.pcb_queue[0]
            self.starttime = max(self.starttime, pcb2.arrivetime)
            if pcb2.runtime <= self.time_chip:                          # 亦即时间片没完，pcb先结束了
                self.starttime += pcb2.runtime                          # self.starttime = self.starttime + pcb.runtime
                pcb2.finishtime = self.starttime
                pcb2.zztime = pcb2.finishtime - pcb2.arrivetime
                pcb2.weightzztime = round(pcb2.zztime / pcb2.runtime, 3)
                pcb2.runtime += pcb2.temp * self.time_chip
                pcb2.finished = True
                self.over = self.pcb_queue.pop(0)
                # 找出在下一个pcb开始之前已到达的pcb，塞进就绪队列排队
                self.pcb_list, self.pcb_queue, flag = self.find_ready_pcb(self.pcb_list, self.pcb_queue)
                if not flag and not self.pcb_queue:                      # 如果时间片结束（或者进程over）
                    if self.pcb_list:
                        self.pcb_queue.append(self.pcb_list[-1])
                self.over_list.append(self.over)
            else:
                self.starttime += self.time_chip  #
                pcb2.runtime -= self.time_chip
                self.out = self.pcb_queue.pop(0)
                pcb2.temp += 1
                # 找出在下一个pcb开始之前已到达的pcb，塞进就绪队列排队
                self.pcb_list, self.pcb_queue, flag = self.find_ready_pcb(self.pcb_list, self.pcb_queue)
                self.pcb_queue.append(self.out)

            finished_list = [(x.name, x.finished) for x in self.over_list]
            print("所有进程的over情况：", finished_list)
            if not self.pcb_queue and not self.pcb_list:
                print("所有pcb都over了！！！\n")
                self.output_rr(self.over_list)
                print("\n时间片：{}s".format(self.time_chip))
                break
            else:
                print("继续")

    # 找出在下一个pcb开始之前已到达的pcb，塞进就绪队列排队
    def find_ready_pcb(self, pcblist, pcbqueue, flag=0):
        for i in range(len(pcblist) - 1, -1, -1):                       # 最后一个元素（先到达的元素）开始
            pcb1 = pcblist[i]
            print(pcb1.name, end=" ")
            if pcb1.arrivetime <= self.starttime:                        # 找到所有在下一个开始时间之前到达的pcb，塞进就绪队列
                pcbqueue.append(pcb1)
                pcblist.pop(-1)
                flag = 1
            else:                                                   # 如果下一个进程的理论开始时间之前没有pcb到达，就绪队列不轻举妄动
                break                                               # 因为有序。一旦大于，立马结束循环
        return pcblist, pcbqueue, flag

    def output_rr(self, pcb_list):
        print("进程 pcb_name", "到达时间arriveTime", "服务时间runtime", "完成时间finishtime", "   周转时间zztime",
              "   带权周转时间weightzztime", sep=" \t")
        for pcb3 in pcb_list:
            print("  \t" + str(pcb3.name), pcb3.arrivetime, pcb3.runtime, pcb3.finishtime, pcb3.zztime,
                  pcb3.weightzztime,
                  sep="  \t\t\t\t ")

if __name__ == '__main__':
    r = RR()

