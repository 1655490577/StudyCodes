from socket import *
from multiprocessing import Process
from threading import Thread
import os

class myProcess(Process):
    def __init__(self, cSocket, cServerInfo):
        super().__init__()
        self.cSocket = cSocket
        self.cServerInfo = cServerInfo

    def run(self):
        t1 = Thread(target=self.recv)
        t2 = Thread(target=self.send)
        t1.start()
        t2.start()

    def recv(self):
        while True:
            recvData = self.cSocket.recv(1024)
            if len(recvData)>0:
                recvData = recvData.decode('gb2312')
                print(f'Recived from{self.cServerInfo}:{recvData}')
            else:
                break
        print(f'进程--------pid is{os.getpid()}--结束')
        self.cSocket.close()
        # p1.close()

    def send(self):
        while True:
            # print('<<<<<<')
            try:
                send_data = input('<<<<')
            except EOFError:
                break
            print('------111-------')
            if send_data != '':
                sSocket.send(send_data.encode('gb2312'))
            else:
                continue

if __name__ == '__main__':
    sSocket = socket(AF_INET, SOCK_STREAM)
    sSocket.bind(('', 7788))
    sSocket.listen(5)
    while True:
        cSocket, cServerInfo = sSocket.accept()
        p1 = myProcess(cSocket, cServerInfo)
        p1.start()
        # print(cSocket)
        # print(cServerInfo)
        # p1 = Process(target=recv, args=(cSocket, cServerInfo,))
        # p2 = Process(target=send, args=(cSocket, cServerInfo,))
        # p1.start()
        # p2.start()