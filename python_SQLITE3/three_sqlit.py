import random
import sqlite3
int_one = random.randint(0, 10)
int_two = random.randint(0, 10)
conn = sqlite3.connect('my.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1  INTEGER,col_2 INTEGER)''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (int_one,int_two,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

for i in k:
    r = random.choice(i)
    for j in i:
        if j // 2 == 0:
            cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
            conn.commit()
        else:
            cursor.execute('''UPDATE tab_1 SET col_1= 2, col_2= 2 WhERE id=?''')
            conn.commit()