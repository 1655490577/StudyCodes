import struct
from socket import *

ipAddr = '192.168.31.12'
downFileName = '123456.jpg'

myRequest = struct.pack('!H10sb5sb', 1, '123456.jpg'.encode('gb2312'), 0, 'octet'.encode('gb2312'), 0) # 组包
udpSocket = socket(AF_INET, SOCK_DGRAM)
# udpSocket.bind(('', 7878))
udpSocket.sendto(myRequest, (ipAddr, 69))
newFile = open('123456.jpg'.encode('gb2312'), 'wb')
while True:
    recvfromData = udpSocket.recvfrom(1024)
    recvData,serverInfo = recvfromData      # （操作号，块编码），（服务器ip，端口）
    CZnum = struct.unpack('!H', recvData[:2])       # 操作号
    moduleNum = struct.unpack('!H', recvData[2:4])      # 块编码
    if CZnum[0] == 3:
        newFile.write(recvData[4:])
        ackData = struct.pack('!HH', 4, moduleNum[0])
        udpSocket.sendto(ackData, serverInfo)
    if len(recvData) < 516:
        break
newFile.close()
udpSocket.close()
