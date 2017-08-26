import sqlite3
from bottle import route, run, template


@route('/')
@route('/rates')
def main_page(): # Get current coin rates
  con = sqlite3.connect('data.db')
  c = con.cursor()
  c.execute("SELECT name,code,trend,rate FROM exchange")
  res = c.fetchall() # coin rate lookup
  c.close()
  page = template('rates_page', rows=res) # return page
  return page

run(reloader=True)
