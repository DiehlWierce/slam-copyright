"""
MAIN THREAD
Handles all of the connections, creating new games and
requests from the client(s).
"""
import socket
import threading
import time
from .player import Player
from .game import Game
import json


class Server(object):
    PLAYERS = 8
    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        handles in game communication between clients
        :param conn: connection object
        :param ip: str
        :param name: str
        :return: None
        """
        while True:

            try:

                #  Receive request
                data = conn.recv(1024)
                data = json.loads(data)

                # Player is not apart of game
                keys = [key for key in data.keys()]
                send_msg = {key:[] for key in keys}

                for key in keys:
                    if key == -1:  # get game
                        ''
                    elif key == 0:  # guess
                        ''
                    elif key == 1:  # skip
                        ''
                    elif key == 2:  # get chat
                        ''
                    elif key == 3:  # get board
                        ''
                    elif key == 4:  # get score
                        ''
                    elif key == 5:  # get round
                        ''
                    elif key == 6:  # get word
                        ''
                    elif key == 7:  # get skips
                        ''
                    elif key == 8:  # update board
                        ''
                    elif key == 9:  # get round time
                        ''
                    else:
                        raise Exception("Not a valid request")

                conn.sendall(json.dumps(send_msg))

            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()} disconnected", e)
                conn.close()
    #             TODO call player game disconnect method

    def handle_queue(self, player):
        """
        adds player to queue and creates new game if enough players
        :param player: Player
        :return: None
        """
        self.connection_queue.append(player)
        if len(self.connection_queue) >= 8:
            game = Game(self.connection_queue[:], self.game_id)

            for p in self.connection_queue:
                p.set_game(game)

            self.game_id += 1
            self.connection_queue = []

    def authentication(self, conn, addr):
        """
        authentication here
        :param ip: str
        :return: None
        """
        try:
            data = conn.recv(16)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")

            conn.sendall("1".encode())

            player = Player(addr, name)
            self.handle_queue(player)
            threading.thread(targets=self.player_thread, args=(conn, player))

        except Exception as e:
            print("[EXCEPTION] ", e)
            conn.close()

    def connection_thread(self):
        server = ""
        port = 0000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen()
        print("Waiting for a connection, Server Started")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New connection!")

            self.authentication(conn, addr)

if __name__ == "__main__":
    s = Server()
    threading.Thread(target=s.connection_thread)