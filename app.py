from flask import render_template, Flask, request, redirect, url_for
from connection import create_connection
import query


app = Flask(__name__)

@app.route('/')
def index():
    data = query.list_all_users()
    if data:
        return render_template('index.html', title='Backend-Test', members=data)
    return render_template('index.html', title='Backend-Test', members='No data available')

@app.route('/add', methods=['POST'])
def add_users():
    id_user = int(request.form['Id'])
    full_name = request.form['FullName']
    birth = request.form['Birth']
    email = request.form['Email']

    if id_user and full_name and birth and email:
        data = (id_user, full_name, birth, email)
        data_to_insert = query.add_users(data)
        if not data_to_insert:
            return redirect(url_for('index'))

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
