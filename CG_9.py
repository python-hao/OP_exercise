class test8:
    def __init__(self,a,b,*c):
        self.__a = a
        self.__b = b
        self.__c = list(c)
        print("参数为：",self.__a,self.__b,self.__c)
    def sum_num(self):
        return sum(self.__c) +self.__a+self.__b
    def gai(self,v1,v2):
        self.__a = v1
        self.__b = v2
        return self.__a,self.__b


if __name__ == '__main__':
    test = test8(1,2,3,4,4)
    print("求和结果：",test.sum_num())
    print("a、b重新赋值为：",test.gai(1515,1616))
