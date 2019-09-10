#请使⽤Python代码写出验证⽤户登录的装饰器; 要求: 装饰器可以接收函数的参数;
def deco(func):
    def wapps(user,passwd):
        if user=='root' and passwd=='123456':
            func(user,passwd)
        else:
            print("Please enter the correct password!")
    return wapps
@deco
def login(user,passwd):
    print('user={},passwd={}'.format(user,passwd))

login=login('2','123456')