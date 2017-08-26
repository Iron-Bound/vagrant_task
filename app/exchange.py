import sqlite3
from bottle import route, run, debug, template

@route('/')
@route('/rates')
def main_page(): # Get current coin rates
  con = sqlite3.connect('data.db')
  c = con.cursor()
  c.execute("SELECT name, rate FROM exchange")
  res = c.fetchall() # coin rate lookup
  c.close()
  page = template('rates_page', rows=res) # return page
  return page

debug(True)
run(reloader=True)
