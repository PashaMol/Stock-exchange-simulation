# importing the required module 
import matplotlib.pyplot as plt
import sqlite3

def ti_me_table():
  ti_me.execute("CREATE TABLE IF NOT EXISTS ti_me(id REAL, conn REAL, response REAL)")

conn9 = sqlite3.connect('ti_me.db')
ti_me = conn9.cursor()
ti_me_table()
from statistics import median
x = []
y = []

for i in range(1,501):
    ti_me.execute(f"SELECT response FROM ti_me WHERE conn = {i}")
    ans = [k[0] for k in ti_me.fetchall()]
    if len(ans) == 0: continue
    print(f"Mean waiting for {i}: {median(ans)}")
    x.append(i)
    y.append(median(ans))    

# x axis values 

# corresponding y axis values 


# plotting the points 
plt.plot(x, y)
print("XY:", x, y)

# naming the x axis 
plt.xlabel('connections/second') 
# naming the y axis 
plt.ylabel('waitinng time') 

# giving a title to my graph 
plt.title('Stress test') 

# function to show the plot 
plt.show() 
