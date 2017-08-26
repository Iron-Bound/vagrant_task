import sqlite3
conn = sqlite3.connect('data.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE exchange (id INTEGER PRIMARY KEY, name char(50) NOT NULL, rate char(30) NOT NULL)")
conn.execute("INSERT INTO exchange (name,rate) VALUES ('Bitcoin','$4,328.54')")
conn.execute("INSERT INTO exchange (name,rate) VALUES ('Ethereum','$328.73')")
conn.execute("INSERT INTO exchange (name,rate) VALUES ('Litecoin','$50.56')")
conn.execute("INSERT INTO exchange (name,rate) VALUES ('Dogecoin','$1337.00')")
conn.commit()
