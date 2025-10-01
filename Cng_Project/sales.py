from db import get_connection

def record_sale(product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Check stock
    cursor.execute("SELECT stock FROM Products WHERE product_id=%s", (product_id,))
    stock = cursor.fetchone()[0]
    if stock < quantity:
        print("Not enough stock")
        conn.close()
        return

    # Insert sale
    cursor.execute("INSERT INTO Sales (product_id, quantity) VALUES (%s, %s)", (product_id, quantity))
    
    # Update stock
    cursor.execute("UPDATE Products SET stock=stock-%s WHERE product_id=%s", (quantity, product_id))
    conn.commit()
    conn.close()
    print("Sale recorded")
