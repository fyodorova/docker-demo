import sqlite3 
import os 
import time 
 
DB_PATH = os.environ.get("DB_PATH", "/db-volume/mydata.db") 
 
def main(): 
    conn = sqlite3.connect(DB_PATH) 
    cur = conn.cursor() 
    cur.execute("INSERT INTO test(txt) VALUES(?)", (time.ctime(),)) 
    conn.commit() 
    for row in cur.execute("SELECT * FROM test"): 
        print(row) 
    conn.close() 
 
if __name__ == "__main__": 
    main() 
