import psycopg2
import bcrypt

# Connection details (use the same ones from your postgres.py)
DB_PARAMS = {
    "host": "cloudmartdb.cjy4c6csc3wv.us-east-2.rds.amazonaws.com",
    "database": "postgres",
    "user": "cloudmart",
    "password": "D33znutz",
    "port": "5432"
}

def setup_database():
    """Creates the users table if it doesn't exist."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
    )
    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print("Table 'users' is ready.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error setting up table: {error}")
    finally:
        if conn is not None:
            conn.close()

def create_account(username, plain_password):
    """Hashes the password and saves the user to the database."""
    # hashing and salting the password
    bytes_password = plain_password.encode('utf-8')
    hash_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())

    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        
        # Inputing going into RDS
        sql = "INSERT INTO users(username, password_hash) VALUES(%s, %s)"
        cur.execute(sql, (username, hash_password.decode('utf-8')))
        
        conn.commit()
        cur.close()
        print(f"User '{username}' created successfully!")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error creating account: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    setup_database()
    
    # Testing 
    new_user = input("Enter a new username: ")
    new_pass = input("Enter a new password: ")
    create_account(new_user, new_pass)