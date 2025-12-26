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

@app.route('/add_category',methods=['GET','POST'])
def category():
    if request.method=='POST':
        name=request.form["name"]
        spending_limit=request.form["spending_limit"]

        conn=get_db_connection()
        conn.execute("INSERT INTO categories (name,spending_limit) VALUES(?,?)",(name,spending_limit))
        
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    
    return render_template('add_categories.html')

@app.route('/add_expense',methods=['GET','POST'])
def add_expenses():
    conn=get_db_connection()

    if request.method=='POST':
        category_id=request.form['category_id']
        date=request.form['date']
        description=request.form['description']
        amount=request.form['amount']

        conn.execute("INSERT INTO expenses (category_id,date,description,amount) VALUES(?,?,?,?)",
                    (category_id,date,description,amount))
        
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    
    categories=conn.execute("SELECT * FROM categories").fetchall()
    conn.close()

    return render_template('add_expense.html',categories=categories)

if __name__=="__main__":
    app.run(debug=True)
