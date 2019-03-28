import sqlite3

data = [
    ('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str', '10.255.1.1', 255),
    ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str', '10.255.1.2', 255),
    ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str', '10.255.1.3', 255),
    ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str', '10.255.1.4', 255)]

query = "INSERT into switch values (?, ?, ?, ?, ?, ?)"

connection = sqlite3.connect('testDB.db')
cursor = connection.cursor()

#cursor.execute("select * from switch")

for row in data:
    cursor.execute(query, row)

connection.commit()
