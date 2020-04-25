import random
import sqlite3
import time
def fill_demo(tm0, prd):
    conn = sqlite3.connect('C:/coding/projServer/box.db')
    c = conn.cursor()
    #return
    for i in range(0,25):
        t = tm0 + i * 3600 + 50
        for j in range(100):
            b = int(random.random()*100)
            e = b + int(random.random()*200) + 1
            print(b,e)
            p = str(random.randrange(b, e))
            c.execute(f"INSERT INTO box VALUES('{prd}',{p},{t},'buy')")
    conn.commit()

def read():
    conn = sqlite3.connect('C:/coding/projServer/box.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS "box" (
	"product"	TEXT,
	"price"	REAL,
	"time"	REAL,
	"type"	TEXT
);''')
    # c.execute("INSERT INTO orders VALUES(17, 'Meee', 'Limit', 'sell', 'pony', 11, 11, 69420)")
    # fill_demo()
    c.execute('SELECT * FROM box')
    data1 = c.fetchall()
    num = 0
    for el in data1:
        num += 1
        print(el)
    print(str(num) + " elements")

lll = [ "PoniesCo", "DrugsUnited", "ApplesInc", "GasTm", "TEST", "HseCoin"]
tm1 = time.time()
tm0 = tm1 - 24*60*60
print(tm0, tm1)
#82049 elements
for el in lll:
    fill_demo(tm0, el)
read()
