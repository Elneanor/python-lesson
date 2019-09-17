
'''
封装的属性外部的访问方式，用setter,getter
'''
class Member:
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def get__name(self):
        return self.__name
    def get__age(self):
        return self.__age

def main():
    mem = Member()
    mem.set_name("xiaoli teacher")
    mem.set_age(29)
    print("name:%s,age:%d" % (mem.get__name(),mem.get__age()))

if __name__ == "__main__":
    main()

