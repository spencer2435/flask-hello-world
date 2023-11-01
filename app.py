import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://cloud_db_r72t_user:uTywBKnB4zu0zirzaSnmlNdqiG5TWGZa@dpg-cl19vk3mgg9c738bcrng-a/cloud_db_r72t")
    conn.close()
    return "Database Connection Successful"
    
