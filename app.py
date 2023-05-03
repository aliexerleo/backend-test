from flask import render_template, Flask, jsonify
from connection import create_connection
import query


app = Flask(__name__)

@app.route('/members')
def index():
    data = query.list_all_users()
    if data:
        return jsonify({'status':data})

    return jsonify({'status':'error connection'})

# def index():
#     users = [ 'Rosalia','Adrianna','Victoria' ]
#     return render_template('index.html', title='Welcome', members=users)

if __name__ == '__main__':
    app.run(debug=True)
