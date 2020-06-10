"""
Represents a round of the game, storing things like
word, time, skips, drawing player and more.
"""
import time as t
from _thread import *
from .game import Game
from .chat import Chat

class Round(object):
    def __init__(self, word, player_drawing, players, game):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.players_scores = {player:0 for player in players}
        self.time = 75
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        Returns true if ound skipped threshold met
        :return: bool
        """
        self.skips += 1
        if self.skips > len(self.players) - 2:
            return True

        return False

    def get_scores(self):
        """
        returns all the players scores
        """
        return self.scores

    def get_score(self, player):
        """
        gets a specific players scores
        :param player: Player
        :return: int
        """
        if player in self.players_scores:
            return self.players_scores[player]
        else:
            raise Exception("Player not in score list")

    def time_thread(self):
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self, player, wrd):
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
    #         TODO implement scoreing system here

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Players
        :return: None
        """
        # might not be able to use players as key in dict
        if player in self.player_scores:
            del self.players_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player in self.player_drawing:
            self.end_round("Drawing player leaves")

    def end_round(self):
        # TODO implement end_round functionality
        pass