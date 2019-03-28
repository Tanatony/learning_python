import sqlite3
#from pprint import pprint

connection = sqlite3.connect('testDB.db')
cursor = connection.cursor()

cursor.execute('select * from switch')

# while True:
#     next_row = cursor.fetchone()
#     if next_row:
#         print(next_row)
#     else:
#         break

# while True:
# 	rows = cursor.fetchmany(3)
# 	if rows:
# 		pprint(rows)
# 	else:
# 		break

print(cursor.fetchall())
