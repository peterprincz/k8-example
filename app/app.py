from flask import Flask, jsonify
import os
import random
import string
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')

random_number = random.randint(1, 65535)
env_var = os.getenv('ENV_VARIABLE', 'MISSING')

@app.route('/')
def get_records():
    try:
        connection = get_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM example_table")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify({'Application instance': random_number, 'result': results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/create')
def create_record():
    try:
        connection = get_connection()
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=10))
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO example_table (name) VALUES ('{random_string}')")
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'Application instance': random_number, 'result': 'Record created: ' + random_string})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
def get_db_config():
    return f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"

if __name__ == '__main__':
    print(get_db_config())
    app.run(host='0.0.0.0', port=3000)