from db import get_connection

def get_all():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT d.MaDon, k.TenKH, d.NgayLap,
        IFNULL(SUM(c.SoLuong * c.DonGia),0) AS TongTien
        FROM DonHang d
        JOIN KhachHang k ON d.MaKH = k.MaKH
        LEFT JOIN ChiTietDonHang c ON d.MaDon = c.MaDon
        GROUP BY d.MaDon
        """)
        return cursor.fetchall()

def insert(makh, ngaylap):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO DonHang (MaKH, NgayLap) VALUES (%s,%s)",
            (makh, ngaylap)
        )
        madon = cursor.lastrowid
    conn.commit()
    return madon

def delete(madon):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM ChiTietDonHang WHERE MaDon=%s", (madon,))
        cursor.execute("DELETE FROM DonHang WHERE MaDon=%s", (madon,))
    conn.commit()

def get_chitiet(madon):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT m.TenHang, c.SoLuong, c.DonGia,
        (c.SoLuong*c.DonGia) AS ThanhTien
        FROM ChiTietDonHang c
        JOIN MatHang m ON c.MaHang = m.MaHang
        WHERE c.MaDon=%s
        """, (madon,))
        return cursor.fetchall()

def insert_chitiet(madon, mahang, soluong, dongia):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO ChiTietDonHang (MaDon, MaHang, SoLuong, DonGia)
        VALUES (%s,%s,%s,%s)
        """, (madon, mahang, soluong, dongia))
    conn.commit()