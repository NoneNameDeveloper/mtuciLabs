from flask import Flask, render_template, request
import requests
import psycopg2


conn = psycopg2.connect(
	database='service_db',
	user='postgres',
	password='159326',
	host='localhost',
	port='5432'
)

cursor = conn.cursor()
app = Flask(__name__)


@app.route('/login/', methods=['GET'])
def index_handler():
	return render_template('login.html')



@app.route('/login/', methods=['POST'])
def login_handler():

        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
                return "Empty log or pass"

        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s;", (str(username), str(password)))

        records = list(cursor.fetchall())

        if not records:
                return "not exists"
        
        data = {"full_name":records[0][1], "login":records[0][2], "password":records[0][3]}


        return render_template('account.html', data = data)




if __name__=="__main__":
	app.run("0.0.0.0")
