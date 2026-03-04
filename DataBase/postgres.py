from enum import verify

import psycopg2
db_host = "cloudmartdb.cjy4c6csc3wv.us-east-2.rds.amazonaws.com"
db_user = "cloudmart"
db_password = "D33znutz"
db_name = "postgres"

connection= psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

print("Database connection successful!")
cursor = connection.cursor()
cursor.execute("SELECT version();")
db_version = cursor.fetchone()

DB_CONFIG = {
    "host": "cloudmartdb.cjy4c6csc3wv.us-east-2.rds.amazonaws.com",
    "database": "postgres",
    "user": "cloudmart",
    "password": "D33znutz", 
    "port": 5432
}

def create_table():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password TEXT NOT NULL
            );
        """)
        conn.commit()
        print("Success: Table 'users' created!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals():
            cur.close()
            conn.close()

if __name__ == "__main__":
    create_table()

# Call this at the very beginning of your main() function
print(f"PostgreSQL Database Version: {db_version[0]}")
# Close the database connection
cursor.close()

