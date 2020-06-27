import time
import threading
import sqlite3
import random
from datetime import datetime


global ti_me
ti_me = time.time() - 3600*30
def time_skip():
  global ti_me
  ti_me = time.time() - 3600*24
  for i in range(26):
    time.sleep(7.5)
    ti_me += 3600
    #if ti_me - time.time() >= 3600*24: exit()
    
global t
t = threading.Thread(target=time_skip, name='Time_skip', daemon = True)
t.start()

def box_table():
  b.execute("CREATE TABLE IF NOT EXISTS box(product TEXT, best_bid REAL, best_ask, time REAL)")

global conn2
conn2 = sqlite3.connect('box.db')
b = conn2.cursor()
box_table()

products = ['GasTm', 'PoniesCo']

while ti_me - time.time() < 0:
    print("TI_ME:", datetime.fromtimestamp(ti_me), "\n\n\n")
    for product in products:
        b.execute(f"INSERT INTO box VALUES('{product}', {random.randrange(0,100)}, {random.randrange(0,100)}, {ti_me})")
    time.sleep(0.1)
conn2.commit()
