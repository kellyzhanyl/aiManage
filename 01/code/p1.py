import time

class Person():
    def __init__(self,username,age,address):
        """
        构造函数
        """
        self.username=username
        self.age=age
        self.address=address
    def cat(self,name):
        self.username=name+self.username
p=Person('zyl','20','beijing')
print(p.username)

class China(Person):
    def __init__(self, username, age, address):
        """
        继承父类
        """
        super().__init__(username, age, address)
    def language(self):
        """
        docstring
        """
        print("语言")
c=China('zhaon','24','shanghai')
print(c.username)
def get_current_time():
    """
    获取当前时间
    """
    now_itme=time.localtime()
    str_time=time.strftime('%Y-%m-%d, %H:%M:%S',now_itme)
    print(str_time)
get_current_time()
