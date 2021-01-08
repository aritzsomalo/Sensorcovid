from flask import Flask, render_template
import FINALDEF
import mariadb

temp = FINALDEF.temperatura()
pres = FINALDEF.presencia()
rfid = FINALDEF.tarjeta()
app = Flask(__name__)


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'flameslinger',
    'database': 'covid'
}
consulta = f'INSERT INTO mediciones.temp (id, temperatura) VALUES ({rfid},{temp})'
consulta2 = 'SELECT * FROM covid.tablatemp'

conn = mariadb.connect(config)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medidor')
def temp():
    
    cur = conn.cursor()
    cur.execute(consulta)
    cur.execute(consulta2)
    res = cur.fetchall()
    
    if rfid != null and press == 1:        
        temperatura = str(temp)
    else:
        temperatura = 'No hay presencia'
    return render_template('medidor.html', temp=temperatura, id_ = rfid)

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
    print(rfid)
    app.run(debug=True, host='0.0.0.0')
