from flask import render_template, Flask
app = Flask(__name__)

@app.route('/members')
def index():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('index.html', title='Welcome', members=users)

app.run(host='0.0.0.0', port=81)