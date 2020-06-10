"""
Reprsents and stores information about the chat
"""

from .round import Round


class Chat(object):

    def __init__(self):
        self.content = []
        self.round = r

    def update_chat(self, msg):
        return self.content

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return "".join(self.content)

    def __repr__(self):
        return str(self)