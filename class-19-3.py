
class Member:
    pass

def main():
    dir_list = dir(Member)

    for item in dir_list:    #找出dir()中关于member类是否有默认的无参构造方法__init__
        if item == "__init__":
            print("找到member类中的无参默认构造方法了")

if __name__ == "__main__":
    main()
