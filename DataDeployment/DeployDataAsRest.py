from flask import Flask, jsonify
import pyodbc

conn_str = 'DRIVER={SQL Server};SERVER=localhost;DATABASE=master;UID=datadeployer;PWD=ErtyYtre1726354;'

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM onpremdata..test1")
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
