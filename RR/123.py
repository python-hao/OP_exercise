
import random
from functools import reduce

Job_Num = int(input("请输入进程数："))        #进程数
ArrivalTime = [0 for _ in range(Job_Num)]   #到达时间
ServiceTime = [0 for _ in range(Job_Num)]   #服务时间
FinishTime = [0 for _ in range(Job_Num)]    #完成时间
zzTime = [0 for _ in range(Job_Num)]        #周转时间
WeightzzTime = [0 for _ in range(Job_Num)]  #带权周转时间
Finished = [False for _ in range(Job_Num)]  #进程标志，是否已经执行完了
Job_Set = []    #进程列表，输入的顺序写入，只是暂时存着进程，接下来按到达时间排序后放在就绪队里里面
Job_Queue = []  #就绪队列


def initial():
    """初始化"""
    global ArrivalTime, ServiceTime, Job_Set
    ArrivalTime = random.sample(range(Job_Num), Job_Num)    #一下子挑出五个随机到达时间
    ServiceTime = random.sample(range(1, 26), Job_Num)      #一下子挑出五个随机服务时间
    print('请输入{}个作业的名字'.format(Job_Num))
    # # 构造一个循环队列
    # job = Job('head')
    # job_head = None     #job_head 头节点
    for i in range(Job_Num):
        name = input()
        Job_Set.append(name)


def output_rr():
    print("进程 Job_Queue","到达时间ArrivalTime","服务时间ServiceTime","完成时间FinishTime","   周转时间zzTime","   带权周转时间WeightzzTime",sep=" \t")
    for i in Job_Queue:
        print("  \t"+str(Job_Set[Job_Queue[i]]),ArrivalTime[i],ServiceTime[i],FinishTime[i],zzTime[i],WeightzzTime[i],sep="    \t\t\t\t ")
    print("\n平均周转时间:{}".format(round(sum(zzTime)/Job_Num), 2))
    print("平均带权周转时间:{}".format(round(sum(WeightzzTime)/Job_Num), 2))     #round()四舍侮辱函数

def rr():
    """引用全局变量"""
    global Job_Queue, ServiceTime, Finished, WzzTime, WeightzzTime, FinishTime
    time_chip = float(input("input time_chip:"))    #时间片大小
    arrival_copy = ArrivalTime.copy()       #复制一个到达时间列表，用于对Job_Set进行FCFS排序
    service_copy = ServiceTime.copy()       #同上
    #对arrival_copy列表排序找出索引，然后顺序加入Job_Queue就绪队列里面
    for i in range(Job_Num):
        min_t = min(arrival_copy)
        arrival_copy.remove(min_t)
        #找出最小到达时间对应job在原ArrivalTime列表的位置
        for j in range(Job_Num):
            if min_t == ArrivalTime[j]:
                Job_Queue.append(j)
                break
    real_time = 0  # 当前的结束时间，下一个进程的开始时间
    count = 0
    while count < Job_Num:
        #如果当前进程的剩余服务时间小于时间片，且还未完成运行
        if service_copy[Job_Queue[count]] <= time_chip and not Finished[Job_Queue[count]]:
            real_time += service_copy[Job_Queue[count]]
            FinishTime[Job_Queue[count]] = round(real_time, 5)
            zzTime[Job_Queue[count]] = round(real_time - ArrivalTime[Job_Queue[count]],5)
            WeightzzTime[Job_Queue[count]] = round(zzTime[Job_Queue[count]]/ServiceTime[Job_Queue[count]], 5)
            Finished[Job_Queue[count]] = True
        #若当前作业未完成，则到队尾，时间加上
        elif not Finished[Job_Queue[count]]:
            real_time += time_chip
            service_copy[Job_Queue[count]] -= time_chip
        count += 1
        #判断进程是否都已经完成了，若已经都完成，则输出所有进程信息
        if reduce(lambda x, y: x & y, Finished):
            print('所有作业完成!!')
            #输出进程信息
            output_rr()
            break
            #判断进程是否都已经完成了，若还有未完成的，则继续循环，从对头开始
        if not reduce(lambda x, y: x & y, Finished) and count == Job_Num:
            count = 0

if __name__ == '__main__':
    initial()
    rr()
