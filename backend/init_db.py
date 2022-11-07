import sqlite3

connection = sqlite3.connect('database.db')


cur = connection.cursor()
cur.execute("DROP TABLE IF EXISTS GOLD")
cur.execute("""CREATE TABLE GOLD(
name TEXT,
purity TEXT,
price TEXT
)""")
cur.execute("INSERT INTO GOLD VALUES('laxmi','22k','50')")
cur.execute("""ALTER TABLE GOLD
            ADD Email TEXT
            """
            )
cur.execute("""UPDATE GOLD
SET Email = 'a@mail'
WHERE name = 'laxmi';
""")
cur.execute("""ALTER TABLE GOLD
            ADD image_url TEXT
            """
            )
cur.execute("""UPDATE GOLD
SET image_url = 'a@mail'
WHERE name = 'laxmi';
""")
cur.execute("""UPDATE GOLD
SET image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s'
WHERE name = 'laxmi';
""")
cur.execute("INSERT INTO GOLD VALUES('alukkas','22k','50','A@mail','ww.')")

cur.execute("DROP TABLE IF EXISTS gold_list")
cur.execute("""CREATE TABLE gold_list(
image_urls TEXT,
name TEXT,
category TEXT,
price TEXT
)""")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin + ganesha','SAFE GOLD','6053.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','MMTC-PAMP','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
cur.execute("INSERT INTO gold_list VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRadrrwOL7DbM_8AZgNRmwFeRyQBKbBHPsKZVK91LERYQ&s','0.5 gm Lakshmi Coin','SAFE GOLD','3069.93')")
connection.commit()
connection.close()
