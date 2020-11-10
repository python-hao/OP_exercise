import math
# 第2题
class MyMath:
    def __init__(self):
        self.__r = int(input("请输入半径："))
    def yuan(self):
        c = round(2*math.pi * self.__r,2)
        s1 = round(math.pi * math.pow(self.__r, 2),2)
        print("圆的周长：{}\n圆的面积：{}".format(c, s1))
    def qiu(self):
        s = round(4* math.pi*math.pow(self.__r,2),2)
        v =round( 4* math.pi*math.pow(self.__r,3)/3,2)
        print("球的表面积：{}\n球的体积：{}".format(s,v))

if __name__ == '__main__':
    mymath = MyMath()
    mymath.yuan()
    mymath.qiu()
# # 第3题
# class Temperature:
#     def __init__(self):
#         self.degree = 0
#
#     def ToFahrenheit(self):
#         self.degree = int(input("请输入摄氏温度："))
#         Fa = self.degree + 56
#         print("摄氏温度={},华氏温度={}".format(self.degree,Fa))
#     def ToCelsius(self):
#         self.degree = int(input("请输入华氏温度："))
#         Ce = self.degree - 56
#         print("华氏温度={},摄氏温度={}".format(self.degree,Ce))
#
# if __name__ == '__main__':
#     temperature = Temperature()
#     temperature.ToFahrenheit()
#     temperature.ToCelsius()