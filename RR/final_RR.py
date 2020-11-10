#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： XHao
# datetime： 2020/11/9 21:46 
# ide： PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： XHao
# datetime： 2020/11/2 21:57
# ide： PyCharm
import random
import time
# 进程信息，封装类成结构体，类似C语言
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
# RR算法封装成类
class RR:
    def __init__(self):
        self.pcb_num = int(input("请输进程数量："))    #进程数
        self.pcb_list = []                          # 进程列表（按输入顺序）
        self.pcb_queue = []                         # 就绪队列
        for i in range(self.pcb_num):
            pcb = Pcb()
            pcb.name = str(input("麻烦老哥输入第{}个pcb的名字：".format(i + 1)))
            self.pcb_list.append(pcb)
        print("~~~~~进程信息~~~~~：")
        self.output_rr(self.pcb_list)
        self.rr()

    def rr(self):
        self.time_chip = float(input("请输入时间片大小："))              # 时间片大小
        self.pcb_list.sort(key=lambda x: x.arrivetime, reverse=True)  # pcb列表元素按到达时间排个队,从大到小（方便后面pop出去）
        self.over_list = []                             # 已经结束的pcb集合
        self.pcb_queue.append(self.pcb_list[-1])        # 就绪队列初始化
        self.pcb_list.pop(-1)                           # 第一个到达的默认已经就绪，所以pop出去
        self.starttime = self.pcb_queue[0].arrivetime   # 第一个pcb的开始时间
        while(True):
            pcb2 = self.pcb_queue[0]
            # 因为后面默认下一个pcb开始时间是当前pcb结束或者被抢占的时间，可能有一种情况：当前结束（完全over），下一个还未到，那么系统会等待
            # 这时候下一个的开始时间，就不是当前的结束时间了，所以加了下面的语句调节一下
            self.starttime = max(self.starttime, pcb2.arrivetime)
            t = self.starttime
            if pcb2.runtime <= self.time_chip:                          # 亦即时间片没完，pcb先结束了
                self.starttime += pcb2.runtime                          # self.starttime = self.starttime + pcb.runtime
                pcb2.finishtime = self.starttime
                pcb2.zztime = pcb2.finishtime - pcb2.arrivetime
                pcb2.weightzztime = round(pcb2.zztime / pcb2.runtime, 3)
                pcb2.runtime += pcb2.temp * self.time_chip
                pcb2.finished = True
                self.over = self.pcb_queue.pop(0)                       # 就绪队列队首pcb运行结束，将就绪队列队首的pcb pop进over队列
                # 找出在下一个pcb开始之前已到达的pcb，塞进就绪队列排队
                self.pcb_list, self.pcb_queue, flag = self.find_ready_pcb(self.pcb_list, self.pcb_queue)
                if not flag and not self.pcb_queue:                      # 如果时间片结束（或者进程over）,没有就绪的pcb
                    if self.pcb_list:
                        self.pcb_queue.append(self.pcb_list[-1])
                print(self.over.name, "  执行完毕！")
                self.over_list.append(self.over)
            # 否则即时间片完了，pcb未结束的，此时会被就绪队列的下一个队首pcb抢占，把它放在就绪队列的尾部等待排队
            else:
                self.starttime += self.time_chip                        # 下一个pcb的开始时间（这里不需要max）
                pcb2.runtime -= self.time_chip
                self.out = self.pcb_queue.pop(0)
                pcb2.temp += 1
                # 找出在下一个pcb开始之前已到达的pcb，塞进就绪队列排队
                self.pcb_list, self.pcb_queue, flag = self.find_ready_pcb(self.pcb_list, self.pcb_queue)
                self.pcb_queue.append(self.out)

            finished_list = [(x.name, x.finished) for x in self.over_list]
            print("时间：", t)
            print("所有进程的over情况：", finished_list)
            time.sleep(1)
            if not self.pcb_queue and not self.pcb_list:
                print("......所有pcb都over了！！！\n")
                self.output_rr(self.over_list)
                print("\n时间片：{}s".format(self.time_chip))
                break
            else:
                pass

    # 找出在下一个pcb开始之前已到达的pcb，塞进就绪队列排队
    def find_ready_pcb(self, pcblist, pcbqueue, flag=0):
        for i in range(len(pcblist) - 1, -1, -1):                       # 最后一个元素（先到达的元素）开始
            pcb1 = pcblist[i]
            if pcb1.arrivetime <= self.starttime:                        # 找到所有在下一个开始时间之前到达的pcb，塞进就绪队列
                pcbqueue.append(pcb1)
                pcblist.pop(-1)
                flag = 1
            else:                                                   # 如果下一个进程的理论开始时间之前没有pcb到达，就绪队列不轻举妄动
                break                                               # 因为有序。一旦大于，立马结束循环
        return pcblist, pcbqueue, flag
    # 输出所有进程目前的信息
    def output_rr(self, pcb_list):
        print("进程 pcb_name", "到达时间arriveTime", "服务时间runtime", "完成时间finishtime", "   周转时间zztime",
              "   带权周转时间weightzztime", sep=" \t")
        for pcb3 in pcb_list:
            print("  \t" + str(pcb3.name), pcb3.arrivetime, pcb3.runtime, pcb3.finishtime, pcb3.zztime,
                  pcb3.weightzztime,
                  sep="  \t\t\t\t ")

if __name__ == '__main__':
    r = RR()