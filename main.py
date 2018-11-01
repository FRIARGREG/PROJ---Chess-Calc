# utf-8

"""
Remake of an old chess calculator I made back in 1998
"""
from tkinter import *
import sqlite3

conn = sqlite3.connection("players.db")
curs = conn.cursor()

def rebuild():
    SQLscript = ""
    with open('sqlbuild.sql', 'r') as f:
        SQLscript = f.readlines()
    curs.executescript(SQLscript)


#### function for calculating new score
class player(object):
    self.score = 1000
    self.games_played = 0
    self.provisional = True

    if self.games_played > 10:
        self.provisional = False


    def calculate(**kwargs):
        """  """
        I_Won = kwargs.get('I_Won', False)
        opponent_score = kwargs.get('opponent_score', 1000)

        winner = 1 if I_Won else -1
        winner *= 10 if self.provisional else 1

        self.games_played += 1

        self.my_score += (abs(my_score-opponent_score) * winner)

args = {}
args['my_score'] = 1000
args['opponent_score'] = 1000
args['I_Won'] = True
args['Im_new'] = False




class













""" end """
