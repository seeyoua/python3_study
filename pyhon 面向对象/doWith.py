from socket import socket,AF_INET,SOCK_STREAM
from functools import partial
"""
    一个类支持上下文管理 tcp 的连接方式
"""
class OperatorSockt(object):

    def __init__(self,address,family=AF_INET,type=SOCK_STREAM):
        self.address = address
        self.familay = family
        self.type = type
        self.sockt = None
    def __enter__(self):
        if self.sockt is not None:
            raise RuntimeError("正在运行")

        self.sockt = socket(self.familay,self.type)
        self.sockt.connect(self.address)
        return self.sockt

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sockt.close()
        self.sockt = None

with OperatorSockt(("www.python.org",80)) as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)





class OperatorFile(object):
    def __init__(self,filename):
        self.filename = filename
        self.f = None

    def __enter__(self):
        if self.f is not None:
            raise RuntimeError("文件对象已经创建")

        self.f = open(self.filename,"wb")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        self.f = None

with OperatorFile("123.txt") as f:
    f.write(b"12345")

