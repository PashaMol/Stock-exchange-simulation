import csv
import time
import random as rnd
import sqlite3
import os
import sys
path = os.path.dirname(os.getcwd())
sys.path.append(path)

import mm_client


# initializing

AvailableGoodsFile = open("AvailableGoods.txt", "r")
AvailableGoods = AvailableGoodsFile.read().split('\n')

for i in range(len(AvailableGoods)):
    AvailableGoods[i] = AvailableGoods[i].split('; ')

print(AvailableGoods, end='\n\n')

class Shares:


    def __init__(self, initer):

        # Setting factors

        self.prices = []
        self.name = initer[0]
        self.minIPO = int(initer[1])
        self.maxIPO = int(initer[2])
        self.drift = float(initer[3])
        self.defaultdrift = self.drift
        self.diffusion = float(initer[4])
        
        '''
        self.compl = 
        self.subst =  
        self.status = 
        '''

    def GeneratePrice(self):

        # Generating IPO

        if (len(self.prices) == 0):
            self.prices.append(rnd.randrange(self.minIPO, self.maxIPO))
            self.avgIPO = self.prices[-1] 
            return self.prices[-1]

        # Modifying price

        new_price = self.prices[-1]
        new_price = max(0, new_price + self.avgIPO * rnd.normalvariate(self.drift, self.diffusion))
        self.prices.append(new_price)

        # Modifying price dynamic

        self.drift += 0.1 * rnd.normalvariate(0, 1) * self.defaultdrift;

        return self.prices[-1]
    
    def GenerateQuery(self):


        last_price = self.prices[-1]
        
        if (last_price == 0):
            return "Broke"
        query = [time.time()]
        query.append(rnd.choice(["Limit", "FillOrKill"]))
        query.append(rnd.choice(["sell", "buy"]))
        query.append(self.name)
        query.append(rnd.choice([i for i in range(1, 11)]))
        query.append(int(last_price * 100) / 100)

        return query

Market = [Shares(t) for t in AvailableGoods]

MarketPrices = [[] for t in AvailableGoods]

mm_client.register('MM')

def ti_me_table():
  ti_me.execute("CREATE TABLE IF NOT EXISTS ti_me(id REAL, conn REAL, response REAL)")

conn9 = sqlite3.connect('ti_me.db')
ti_me = conn9.cursor()
ti_me_table()
start = time.time()
sleep_time = 0

for i in range(10000):
    for i in range(len(Market)):
        #time.sleep(0.1)
        MarketPrices[i].append(Market[i].GeneratePrice())
        NewQuery = Market[i].GenerateQuery()
        if (NewQuery != "Broke"):
            time.sleep(sleep_time)
            if time.time() - start >= 1.1:
                sleep_time += (1/last)/(last-1)
                start = time.time()
                print("Last:", last)
                print("Sleeping for:", sleep_time)
                
            st = time.time()
            mm_client.process(NewQuery, 'MM')
            #print("Waited", time.time() - st, "seconds...")
            #print(NewQuery[0])
            ti_me.execute(f"UPDATE ti_me SET response = {time.time() - st} WHERE id = {NewQuery[0]}")
            ti_me.execute(f"SELECT * FROM ti_me WHERE id = {NewQuery[0]}")
            last = ti_me.fetchall()[0][1]
            conn9.commit()
            

    #time.sleep(6.0)

'''
days = np.linspace(1, 100, 100)

for i in range(len(Market)):
    print(Market[i].prices[0])
    plt.plot(days, MarketPrices[i], label=Market[i].name)
    plt.title(Market[i].name)
    plt.show()
'''

