import sqlite3
# text_one = "hello"
# text_two = "world"
int_one = int(input('input integer'))
conn = sqlite3.connect('name1.db')
# Создаем обьект cursor, который позваляет нам взаимодейтвовать с базой данных
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1  TEXT,col_2 TEXT,col_3 INTEGER)''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES ('hello','world',?)''', (int_one,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
for i in k:
    e = 0
    h = list(i)
    m = ' '.join(str(e)for e in h)
    print(m)