import socket
import pickle

class Network:
    def __init__(self):
        # self.client = socket.socket(socket.AF_INET,...)
        self.server = "localhost"
        self.port = 0000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getPlayer(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            # return pickle.loads((self.client.recv(20...)))
        except socket.error as e:
            print(e)