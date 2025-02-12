import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user ON Users (username)")


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()

def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username, ))
    if check_user.fetchone() is None:
        return True
    else:
        return False
def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products_list = cursor.fetchall()
    connection.commit()
    connection.close()
    return products_list



# initiate_db()
#
#
#
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f'Продукт {i}', f'Описание {i}', i*100))



connection.commit()
# connection.close()
