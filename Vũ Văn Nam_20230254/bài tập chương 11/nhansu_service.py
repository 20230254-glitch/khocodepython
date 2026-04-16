import sqlite3

def connect():
    return sqlite3.connect("nhansu.db")

# Thêm
def them(ns):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)
    """, ns)

    conn.commit()
    conn.close()

# Sửa
def sua(ns):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE nhansu
    SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
    WHERE cccd=?
    """, (ns[1], ns[2], ns[3], ns[4], ns[0]))

    conn.commit()
    conn.close()

# Xóa
def xoa(cccd):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM nhansu WHERE cccd=?", (cccd,))

    conn.commit()
    conn.close()

# Lấy danh sách
def get_all():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM nhansu")
    data = cursor.fetchall()

    conn.close()
    return data

# Tìm kiếm
def timkiem(keyword):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM nhansu
    WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

    data = cursor.fetchall()
    conn.close()
    return data