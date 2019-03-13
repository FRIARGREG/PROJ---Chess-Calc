# chess objects and functions

# utf-8

"""
Remake of an old chess calculator I made back in 1998
"""
import tkinter as tk
import sqlite3
# import wrapper_sqlite3

conn = sqlite3.connect("data\\chess.db")


# function for rebuilding the database to zero ##############################
def rebuild():
    curs = conn.cursor()
    SQLscript = ""
    with open('chess.db.sql', 'r') as f:
        SQLscript = f.readlines()
    curs.executescript(SQLscript)


# object for managing players ###############################################
class Player(object):
    def __init__(self, **kwargs):
        self.ID = kwargs.get('ID', "")
        self.name = kwargs.get('name', "")
        self.score = kwargs.get('score', 1000)
        self.games_played = kwargs.get('games_played', 0)
        self.provisional = self.games_played > 10

    def calculate(self, **kwargs):
        """ calculate this players new score """
        I_Won = kwargs.get('I_Won', False)
        opponent_score = kwargs.get('opponent_score', 1000)
        winner = 1 if I_Won else -1
        winner *= 10 if self.provisional else 1
        self.games_played += 1
        self.my_score += int(abs(self.score-opponent_score)/10 * winner)


# object for managing games #################################################
class game(object):
    def __init__(self):
        self.p_WHITE = None
        self.p_BLACK = None
        # result is 0 for tie, 1 for WHITE and 2 for BLACK
        self.result = None


# object for main application window ########################################
class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.curs = conn.cursor()
        self.grid()
        self.create_widgets()

    def create_player(self, ID):
        SQL = """SELECT * FROM players
            WHERE ID = %s;"""

        data = self.curs.execute(SQL).fetchall()

        temp = Player(ID=int(data[0][0]),
                      name=data[0][1],
                      score=int(data[0][2]),
                      games_played=int(data[0][3]))
        return temp

    def save(self, temp):
        SQL = """ UPDATE players SET score = %s, games_played = %s,
            provisional = %s WHERE ID = %s;""" \
            % (temp.score, temp.games_played, temp.provisional, temp.ID)
        self.curs.execute(SQL)
        conn.commit()

    def create_widgets(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar)
        filemenu.add_command(label='New Player', command=self.new_Player)
        filemenu.add_command(label='New Game', command=self.new_Game)

        filemenu.add_command(label='Save', command=self.save)
        filemenu.add_command(label='Reset', command=self.clear)

        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_command(label='Quit', command=tk.root.quit)

        self.lbl_1 = tk.Label(self, text='The Bowling Calculator')
        self.lbl_1.grid(row=0, columnspan=3)

        self.lbl_2 = tk.Label(self, text='Enter score from game 1 ')
        self.lbl_3 = tk.Label(self, text='Enter score from game 2 ')
        self.lbl_4 = tk.Label(self, text='Enter score from game 3 ')
        self.lbl_5 = tk.Label(self, text='Average:')
        self.lbl_2.grid(row=2, column=0)
        self.lbl_3.grid(row=3, column=0)
        self.lbl_4.grid(row=4, column=0)
        self.lbl_5.grid(row=5, column=0)

        self.score_1 = tk.Entry(self)
        self.score_2 = tk.Entry(self)
        self.score_3 = tk.Entry(self)
        self.avg = tk.Entry(self)
        self.score_1.grid(row=2, column=1)
        self.score_2.grid(row=3, column=1)
        self.score_3.grid(row=4, column=1)
        self.avg.grid(row=5, column=1)

        self.btn_1 = tk.Button(self, text='Calculate Average',
                               command=self.calculate)
        self.btn_2 = tk.Button(self, text='Clear Result', command=self.clear)
        self.btn_1.grid(row=6, column=0)
        self.btn_2.grid(row=6, column=1)

        self.score_1.focus_set()
        tk.root.config(menu=menubar)

    def calculate(self):
        numScore_1 = int(self.score_1.get())
        numScore_2 = int(self.score_2.get())
        numScore_3 = int(self.score_3.get())
        total = numScore_1 + numScore_2 + numScore_3
        average = total / 3

        strAverage = "{0:.2f}".format(average)
        self.avg.insert(0, strAverage)

    def clear(self):
        self.score_1.delete(0, tk.END)
        self.score_2.delete(0, tk.END)
        self.score_3.delete(0, tk.END)
        self.avg.delete(0, tk.END)
        self.score_1.focus_set()


# object for main application window ########################################
class choose_player(tk.Frame):
    def __init__(self, master, position):
        super(Application, self).__init__(master)
        self.curs = conn.cursor()
        self.grid()
        self.create_widgets()
        self.position = position

    def create_widgets(self):
        SQL = """ SELECT ID, name FROM players;"""
        data = self.curs.execute(SQL).fetchall()
        names = data[0]
        listheight = len(names) if len(names) < 10 else 10

        self.lbl_1 = tk.Label(self, text='Choose a Player')
        self.lbl_1.grid(row=0, column=0, sticky=W+E)
        self.lst_players = tk.List(self, selecttype=tk.SINGLE,
                                   height=listheight)
        self.lst_players.grid(row=1, column=0, sticky=W+E)

        for name in names:
            self.lst_players.insert(tk.END, name)


""" end """
