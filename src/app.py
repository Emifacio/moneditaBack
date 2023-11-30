from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config ['MYSQL_DATABASE_HOST'] = 'localhost:3306'
app.config ['MYSQL_DATABASE_USER'] = 'root'
app.config ['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config ['MYSQL_DATABASE_DB'] = 'cursos'

mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "insert into cursos (nombre) value ('trading');"
    cursor.execute(sql)

    conn.commit(sql)

    return render_template('cursos/index.html')

if __name__ == '__main__':
    app.run(debug=True)
