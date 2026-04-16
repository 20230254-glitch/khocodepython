from db import get_connection

def get_all():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM KhachHang")
        return cursor.fetchall()

def insert(ten, diachi, sdt):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO KhachHang (TenKH, DiaChi, SoDienThoai) VALUES (%s,%s,%s)",
            (ten, diachi, sdt)
        )
    conn.commit()

def update(ma, ten, diachi, sdt):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE KhachHang SET TenKH=%s, DiaChi=%s, SoDienThoai=%s WHERE MaKH=%s",
            (ten, diachi, sdt, ma)
        )
    conn.commit()

def delete(ma):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM KhachHang WHERE MaKH=%s", (ma,))
    conn.commit()

def search(keyword):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM KhachHang
            WHERE TenKH LIKE %s OR DiaChi LIKE %s OR SoDienThoai LIKE %s OR MaKH LIKE %s
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()