import random


class RR():
    def __init__(self):
        super(RR, self).__init__()
        while True:
            self.p_num = input("请输入进程数：")
            if self.p_num.isdigit():
                self.p_num = int(self.p_num)
                self.p_dict = self.createP()
                self.lunzhuanP(self.p_dict, self.p_num)

            else:
                print("输入的不是有效数字")

    def createP(self):
        """
        创建字典，根据输入的进程数进行创建进程字典，时间为随机1-9s之间
        """

        self.p_dict = {}
        # 获取一个a-z的列表,ord():以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
        # chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
        alphabet_list = list(map(chr, range(ord('a'), ord('z') + 1)))

        for i in range(0, self.p_num):
            # 默认进程名为a-z顺序排序
            self.p_dict[alphabet_list[i]] = random.randint(1, 9)
        return self.p_dict

    def lunzhuanP(self, p_dict, p_num):
        """
        开始轮转
        """
        print("进程名称" + " " * 10 + "每个进程需要工作的时间")
        p_time = {}
        p_list = [[-1 for i in range(4)] for j in range(p_num + 1)]
        # 添加输出头
        p_list[0][0] = "Name"
        p_list[0][1] = "run"
        p_list[0][2] = "req"
        p_list[0][3] = "status"
        z = 1
        for k, v in self.p_dict.items():
            # 将进程初始化设置初始值
            p_list[z][0] = k
            p_list[z][1] = 0
            p_list[z][2] = v
            p_list[z][3] = "R"
            p_time[k] = 0
            z += 1

        for k, v in p_dict.items():
            print(k + "          ", v)
        j = 1
        t = 1
        while True:
            if len(p_list) == 1:
                print("进程执行完毕")
                for k, v in p_time.items():
                    print("进程%s的执行周期为：%s" % (k, v))
                break

            # 判断是否有进程执行完毕
            for y in range(1, len(p_list) - 1):

                if p_list[y][3] == "E":
                    del p_list[y]

            if j <= len(p_list) - 1:

                if p_list[j][1] + 1 <= p_list[j][2]:

                    p_list[j][1] += 1

                    if p_list[j][1] == p_list[j][2]:
                        p_list[j][3] = "E"
                else:

                    del p_list[j]
                    continue

            else:
                j = j - len(p_list) + 1
                continue

            print("cpu时刻: ", t)
            print("正在执行的进程：", p_list[j][0])
            p_time[p_list[j][0]] += 1
            j += 1
            t += 1
            for i in range(len(p_list)):
                print(p_list[i])

    #
    # def main(self):
    #     while True:
    #         self.p_num = input("请输入进程数：")
    #         if self.p_num.isdigit():
    #             self.p_num = int(self.p_num)
    #             self.p_dict =self.createP(self.p_num)
    #             self.lunzhuanP(self.p_dict, self.p_num)
    #
    #         else:
    #             print("输入的不是有效数字")


if __name__ == "__main__":
    RR()
