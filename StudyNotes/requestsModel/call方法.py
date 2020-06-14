class A(object):

    def __init__(self):
        print("init")

    def __call__(self, *args):  # 实例对象被当作函数调用时执行此方法
        print("call")


a = A()
a(1)

