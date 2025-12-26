from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#Db connection======================================================================
def get_db_connection():
    conn = sqlite3.connect("expense_tracker.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    print("Creating db")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        spending_limit REAL
                    )
                """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category_id INTEGER,
                        date TEXT NOT NULL,
                        description TEXT NOT NULL,
                        amount REAL NOT NULL,
                        FOREIGN KEY(category_id) REFERENCES categories(id)
                    )
                """)
    
    conn.commit()
    conn.close()

init_db()
#===================================================================================

@app.route('/')
def index():
    conn=get_db_connection()

    expenses=conn.execute("""
            SELECT expenses.*,categories.name as category_name
            FROM expenses
            LEFT JOIN categories ON expenses.category_id=categories.id    
    """).fetchall()

    categories=conn.execute("""SELECT * FROM categories""").fetchall()

    total_spent=conn.execute("""
            SELECT SUM(amount) as total 
            FROM expenses
    """).fetchone()

    conn.close()

    total=total_spent['total'] if total_spent['total'] else 0

    return render_template('index.html', 
                    expenses=expenses, 
                    categories=categories,
                    total_spent=total)


if __name__=="__main__":
    app.run(debug=True)
