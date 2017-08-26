import sqlite3
from bottle import route, run, debug

@route('/')
@route('/rates')
def main_page():
  con = sqlite3.connect('data.db')
  c = con.cursor()
  c.execute("SELECT name, rate FROM exchange")
  res = c.fetchall()
  return str(res)

run(reloader=True)
