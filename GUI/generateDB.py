import time
import sqlite3
import random

def getRandUnix():
    t = random.random()
    return float(time.time())*t

conn = sqlite3.connect('C:\coding\projServer\ordersBIG.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS orders(reqid REAL, name TEXT, type TEXT, request TEXT, product TEXT, amount REAL, price REAL, uid REAL)")
c.execute('SELECT * FROM orders')

pref_prd = [ "PoniesCo", "DrugsUnited", "ApplesInc", "GasTm", "TEST"]

def fill():
    for prd in pref_prd:
        b, s =0, 0
        while b< 10000:
            b+=1
            c.execute(f"INSERT INTO orders VALUES({getRandUnix()}, 'MM7', 'Limit', 'buy', '{prd}', {random.randint(0,40)},{random.randint(0,15)}, 11)")

        while s < 10000:
            s += 1
            c.execute(
                f"INSERT INTO orders VALUES({getRandUnix()}, 'MM7', 'Limit', 'sell', '{prd}', {random.randint(0,40)},{random.randint(0,15)}, 11)")
#fill()
c.execute('SELECT * FROM orders')

data1 = c.fetchall()
for el in data1:
    print(el)
print(len(data1))
conn.commit()

