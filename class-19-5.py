
class Message:
 #   info = "test for class attribute"
    __slots__ = ("name","age")

def main():
#    print(Message.info)  #调用类属性，类名.属性名
    mem = Message()
    mem.name = "xiaoli"
    mem.age = 19
#    mem.school = "tsing hua" #因为使用了__slots__函数，在类属性中使用元级定义死了只有name,age的这2个属性。所以在实例属性中只能
#引用name,age这2个属性，而school超出了，所以会报错。
    Message.school = "北京大学"  #这个是类属性的扩展，是有效的
    print("name:%s,age:%s,school:%s" % (mem.name,mem.age,Message.school))


if __name__ == "__main__":
    main()


