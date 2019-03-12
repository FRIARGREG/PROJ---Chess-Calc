""" this module is a wrapper for database usage. it ports with the sqlite3
library and provides this application with a simple interface. """

from sqlite3 import *

def get_conn(filename):
    return sqlite3.connect(filename)
