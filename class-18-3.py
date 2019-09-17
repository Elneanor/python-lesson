
class Member:
    '''
    定义一个类，定义了两个实例变量，一个方法get_info
    '''

    def set_info(self,name,age):
        self.name = name
        self.age = age

    def get_info(self):
        return "name:%s,age:%d" % (self.name,self.age)


def main():  #调用类实例化对象。
    mem = Member()
    mem.set_info("jenny",19)
    print(mem.get_info())
    print(type(mem.get_info))  #这个类型是method，是方法，不是function

if __name__ == "__main__":
     main()



