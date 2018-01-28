import pandas as pd
import sqlite3

conn = sqlite3.connect('HangmanSolverdb.db')
c = conn.cursor()
df = pd.read_sql_query("SELECT * from Word_dict", conn)


