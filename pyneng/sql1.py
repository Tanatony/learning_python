import sqlite3
from sqlite3 import Error


# def create_connection(db_file):
#     """Create test connections"""
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#     	conn.close()

# if __name__ == '__main__':
#     create_connection("test_sqlite.db")

def create_connection():
    """create database connection in memory"""
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection()
