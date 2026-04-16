from db import get_connection

def get_all():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM MatHang")
        return cursor.fetchall()

def insert(ten, nguongoc, dongia):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO MatHang (TenHang, NguonGoc, DonGia) VALUES (%s,%s,%s)",
            (ten, nguongoc, dongia)
        )
    conn.commit()

def update(ma, ten, nguongoc, dongia):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE MatHang SET TenHang=%s, NguonGoc=%s, DonGia=%s WHERE MaHang=%s",
            (ten, nguongoc, dongia, ma)
        )
    conn.commit()

def delete(ma):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM MatHang WHERE MaHang=%s", (ma,))
    conn.commit()

def search(keyword):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM MatHang
            WHERE TenHang LIKE %s OR NguonGoc LIKE %s OR MaHang LIKE %s
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()