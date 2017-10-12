import socket
import struct

class SocketTrans(object):
    def __init__(self, serverIp, serverPort):
        self.m_clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.m_clientSocket.connect((serverIp, serverPort))
    def writePara(self, para):
        self.m_clientSocket.send(struct.pack("I", para))
        pass
    
    #waiting for complete...
    def readPara(self):
        pass
    
    #buffeSize -> byte
    def recvData(self,  bufferSize):
        data = self.m_clientSocket.recv(bufferSize)
        return data



