from db import get_connection

def add_product(name, price, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    conn.commit()
    conn.close()

def list_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_stock(product_id, new_stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET stock=%s WHERE product_id=%s", (new_stock, product_id))
    conn.commit()
    conn.close()
