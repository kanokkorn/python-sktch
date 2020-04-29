import sqlite3
from pathlib import Path
from sqlite3 import Error

def create_db(db_file):
  conn = None
  try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()

if __name__ == "__main__":
  local = Path.cwd()
  local / 'sql' / 'test.db'
  print(local)