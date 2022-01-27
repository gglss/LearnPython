# 多线程

from  threading import Thread    #线程类

# 方法一
# def func():
#     for i in range(5):
#         print("主线程",i)
# if __name__ == "__main__":
#     t = Thread(target=func) #
#     t.start() #
#     for i in range(5):
#         print("子线程", i)

# 方法二
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("子线程", i)

if __name__ == "__main__":
    t = MyThread()
    t.start()
    for i in range(5):
        print("主线程", i)

