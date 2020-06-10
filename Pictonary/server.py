import socket
from _thread import *
from playert import Player
import pickle

server = ""
port = 0000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(100,50, 50, 50), Player(300, 50, 50, 50)]
def threaded_client(conn, player):
    send = pickle.dumps(players[player])
    conn.send(send)

    send = ""
    while True:
        try:
            data = conn.recv(2048)
            obj = pickle.loads(data)
            players[player] = obj

            if not data:
                print("Disconnected")
                break
            else:
                print("Received form player", player)
                print("Sending to player", player)
                if Player == 1:
                    send = players[0]
                else:
                    send = players[1]
            send = pickle.dumps(send)
            conn.sendall(send)
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1


