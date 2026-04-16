import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="vuvannam",  
        database="quanlybanhang",
        cursorclass=pymysql.cursors.DictCursor
    )