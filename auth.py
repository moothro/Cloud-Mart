import psycopg2
import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for

# 1. Keep your connection details
DB_PARAMS = {
    "host": "cloudmartdb.cjy4c6csc3wv.us-east-2.rds.amazonaws.com",
    "database": "postgres",
    "user": "cloudmart",
    "password": "D33znutz",
    "port": "5432"
}

auth = Blueprint('auth', __name__)

def create_account(username, plain_password):
    """Hashes the password and saves the user to the database."""
    bytes_password = plain_password.encode('utf-8')
    hash_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())

    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        sql = "INSERT INTO users(username, password_hash) VALUES(%s, %s)"
        cur.execute(sql, (username, hash_password.decode('utf-8')))
        conn.commit()
        cur.close()
        return True
    except Exception as error:
        print(f"Error: {error}")
        return False
    finally:
        if conn:
            conn.close()

@auth.route('/signup', methods=['GET', 'POST']) # Renamed to signup
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Use your custom function instead of SQLAlchemy's db.session
        success = create_account(username, password)
        
        if success:
            return redirect(url_for('main.profile'))
        else:
            return "Error creating account", 400

    return render_template('signin.html')