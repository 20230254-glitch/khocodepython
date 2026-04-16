import sqlite3

def connect():
    return sqlite3.connect("nhansu.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhansu (
        cccd TEXT PRIMARY KEY,
        hoten TEXT,
        ngaysinh TEXT,
        gioitinh TEXT,
        diachi TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()