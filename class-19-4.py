
class Member:
    def __init__(self,**kwargs): #kwargs关键字参数，是一个map
        print("[构造方法]实例化新对象，当前对象的地址：%s" % id(self))
        self.__name = kwargs.get("name")
        self.__age = kwargs.get("age")
    def __del__(self):
        print("析构方法资源被释放，当前对象的地址：%s" % id(self))
    def get_info(self):
        return "name:%s, age:%s" % (self.__name,self.__age)

def main():
    # mem_a = Member(name="mem-a",age=18)
    mem_a = Member()
    # print(mem_a.get_info())
    mem_b = Member(name="mem-a",age=18)
    # print(mem_b.get_info())
    # mem_c = Member(age=22)
    # print(mem_c.get_info())
    print("对象实例化mem_a的地址：%s,mem_b地址：%s" % (id(mem_a),id(mem_b)))
    del mem_b     #对象回收前会调用析调方法进行收尾处理。
    print(mem_a.get_info())

if __name__ == "__main__":
    main()


#执行结果：
# name:mem-a, age:18
# # name:mem-b, age:None
# # name:None, age:22