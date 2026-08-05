import sqlite3
def create_expenses_table():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS expenses(title TEXT, amount REAL, category TEXT)')
    connection.commit()
    connection.close()

def store_expenses(title , amount ,category):
    connection=sqlite3.connect("data.db")
    cursor=connection.cursor()
    cursor.execute(
        'INSERT INTO expenses(title, amount, category) Values(?,?,?)',
    (title, amount, category) ) 
    connection.commit()
    connection.close()
    
def extract_expenses_data():
    connection=sqlite3.connect("data.db")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM expenses')
    expenses=cursor.fetchall()
    connection.close()
    return expenses
