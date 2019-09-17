
class Member:
    '''
    属性如何封装，在属性名称前加上两个下划线。
    如果属性被封装后，在外面就不能直接访问了
    '''
    def set_info(self,name,age):
        self.__name = name
        self.__age = age

def main():
    mem = Member()
    mem.set_info("xiaoli",19)
    print(mem.name)   #属性被封装了，这里外部调用就报错。AttributeError: 'Member' object has no attribute 'name'
    print(mem.age)

if __name__ == '__main__':
    main()



