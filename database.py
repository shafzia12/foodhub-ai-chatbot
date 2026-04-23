import sqlite3

conn = sqlite3.connect("orders.db", check_same_thread=False)

def fetch_order(order_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
    return cursor.fetchone()