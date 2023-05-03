from flask import render_template, Flask, jsonify
from connection import create_connection
import query


app = Flask(__name__)

@app.route('/')
def index():
    data = query.list_all_users()
    if data:
        return render_template('index.html', title='Backend-Test', members=data)
    return render_template('index.html', title='Backend-Test', members='No data available')

if __name__ == '__main__':
    app.run(debug=True)
