import sqlite3

conn = sqlite3.connect('coso_base') 
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS Users
          ([user_id] INTEGER PRIMARY KEY, [name] TEXT)
          ''')

conn.commit()


# For testing

c.execute('''
          INSERT INTO Users (user_id, name)

                VALUES
                (1,'Pepito'),
                (2,'Fulanito'),
                (3,'Menganito')
                
          ''')

conn.commit()


c.execute('''
          SELECT
          * from Users
          ''')

print(c.fetchall())