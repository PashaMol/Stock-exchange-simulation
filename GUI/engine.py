import sqlite3
import csv
import time


def process(b):
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()

    def fill_demo():
        c.execute("INSERT INTO orders VALUES(1, 'Mike', 'Limit', 'sell', 'drugs', 10, 9, 111)")
        c.execute("INSERT INTO orders VALUES(2, 'Sike', 'Limit', 'sell', 'drugs', 10, 12, 222)")
        c.execute("INSERT INTO orders VALUES(3, 'Daniil', 'Limit', 'sell', 'drugs', 4, 7, 333)")
        c.execute("INSERT INTO orders VALUES(4, 'Lgbt', 'FillOrKill', 'sell', 'pony', 10, 12, 444)")
        c.execute("INSERT INTO orders VALUES(5, 'Somebody', 'FillOrKill', 'buy', 'drugs', 3, 20, 555)")
        c.execute("INSERT INTO orders VALUES(6, 'Once', 'Limit', 'buy', 'drugs', 12, 16, 666)")
        c.execute("INSERT INTO orders VALUES(7, 'Told', 'FillOrKill', 'buy', 'drugs', 15, 15, 777)")
        c.execute("INSERT INTO orders VALUES(8, 'Me', 'Limit', 'buy', 'drugs', 12, 13, 888)")

    def create_table():
        c.execute(
            "CREATE TABLE IF NOT EXISTS orders(reqid REAL, name TEXT, type TEXT, request TEXT, product TEXT, amount REAL, price REAL, uid REAL)")

    def show_selected():
        data = c.fetchall()
        for i in data:
            print(i)
        print()

    def delete_all():
        c.execute("DELETE FROM orders")

    def print_table():
        c.execute("SELECT * FROM orders")
        show_selected()

    create_table()
    # delete_all()
    # fill_demo()
    # print_table()

    reqid = float(time.time())
    '''
    with open('input.csv', 'r') as i:
      a = csv.reader(i)
      b = list(a)[0]
    '''
    # print(reqid, b)
    # print()
    from_u = b[0]
    uid = b[1]
    if b[2].lower() == 'limit':
        limit = True
    else:
        limit = False
    if b[3] == 'buy':
        buy = True
    else:
        buy = False
    product = b[4]
    amount = b[5]
    price = b[6]

    transaction_list = []
    list_counter = 0
    total = 0
    q = float(amount)

    if buy:
        c.execute(
            "SELECT * FROM orders WHERE request = 'sell' AND product = " + "\'" + product + "\'" + " AND price <= " + price + " ORDER BY price")
        for i in c.fetchall():
            if q == 0:
                break
            if i[5] > q:
                total += q * i[6]
                transaction_list.insert(list_counter, [reqid, i[0], float(uid), i[7], q, q * i[6]])
                c.execute("UPDATE orders SET amount = '" + str(i[5] - q) + "' WHERE reqid =" + "\'" + str(i[0]) + "\'")
                q = 0
                list_counter += 1
                break
            else:
                q -= i[5]
                total += i[5] * i[6]
                transaction_list.insert(list_counter, [reqid, i[0], float(uid), i[7], i[5], i[5] * i[6]])
                c.execute("DELETE FROM orders WHERE reqid =" + "\'" + str(i[0]) + "\'")
                list_counter += 1
        if q != 0 and limit:
            c.execute("INSERT INTO orders VALUES(" + str(reqid) + ", '" + from_u + "', '" + b[2] + "', '" + b[
                3] + "', '" + product + "', " + str(q) + ", " + price + ", " + uid + ")")

    else:
        c.execute(
            "SELECT * FROM orders WHERE request = 'buy' AND product = " + "\'" + product + "\'" + " AND price >= " + price + " ORDER BY price DESC")
        for i in c.fetchall():
            if q == 0:
                break
            if i[5] > q:
                total += q * i[6]
                transaction_list.insert(list_counter, [i[0], reqid, i[7], float(uid), q, q * i[6]])
                c.execute("UPDATE orders SET amount = '" + str(i[5] - q) + "' WHERE reqid =" + "\'" + str(i[0]) + "\'")
                q = 0
                list_counter += 1
                break
            else:
                q -= i[5]
                total += i[5] * i[6]
                transaction_list.insert(list_counter, [i[0], reqid, i[7], float(uid), i[5], i[5] * i[6]])
                c.execute("DELETE FROM orders WHERE reqid =" + "\'" + str(i[0]) + "\'")
                list_counter += 1

        if q != 0 and limit:
            c.execute("INSERT INTO orders VALUES(" + str(reqid) + ", '" + from_u + "', '" + b[2] + "', '" + b[
                3] + "', '" + product + "', " + str(q) + ", " + price + ", " + uid + ")")

    # print()
    # print("Total Cost:" ,total, '\n')
    print("Resulting data base:")
    print_table()
    # print("\nFINISHED\n")
    conn.commit()
    c.close()
    conn.close()
    print("Transaction List (buy trans.id, sell trans.id, buyer, seller, amount, total):")
    return transaction_list

