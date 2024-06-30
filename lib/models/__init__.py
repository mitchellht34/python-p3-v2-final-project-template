import sqlite3

CONN = sqlite3.connect('gift_ideas.db')
CURSOR = CONN.cursor()
