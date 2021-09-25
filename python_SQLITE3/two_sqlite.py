import random
import sqlite3
int_one = random.randint(0,9)
int_two = random.randint(0,9)
conn = sqlite3.connect('name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1  INTEGER,col_2 INTEGER)''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (int_one,int_two,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
h=0
for i in k:
    for j in i:
        h+=j
g = h /len(k)*2
print(h)
print(g)

