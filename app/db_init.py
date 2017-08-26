import sqlite3
conn = sqlite3.connect('data.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE exchange (id INTEGER PRIMARY KEY, name char(50) NOT NULL, code char(10), trend char(10), rate char(30) NOT NULL)")
conn.execute("INSERT INTO exchange (name,code,trend,rate) VALUES ('Bitcoin','BTC','UP','$4,328.54')")
conn.execute("INSERT INTO exchange (name,code,trend,rate) VALUES ('Bitcoin Cash','BCH2','UP','$4,328.54')")
conn.execute("INSERT INTO exchange (name,code,trend,rate) VALUES ('Ethereum','ETH','DOWN','$328.73')")
conn.execute("INSERT INTO exchange (name,code,trend,rate) VALUES ('Litecoin','LTC','UP','$50.56')")
conn.execute("INSERT INTO exchange (name,code,trend,rate) VALUES ('Dogecoin','DOGE','HOLD','$1337.00')")
conn.commit()
