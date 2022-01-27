from multiprocessing import Process

# 方法1

# def func():
#     for i in range(5):
#         print('子进程', i)
#
# if __name__ == '__main__':
#     t1 = Process(target=func())
#     t1.start()
#     for i in range(5):
#         print('主进 程', i)


def func(name):
    for i in range(5):
        print(name, i)

if __name__ == '__main__':
    t1 = Process(target=func, args=("周杰伦",))  # args传参必须是元组
    t1.start()

    t2 = Process(target=func, args=("王力宏",))
    t2.start()