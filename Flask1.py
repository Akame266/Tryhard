from faker import Faker
from flask import Flask

app = Flask(__name__)


@app.route('/avr_data')
def func():
    a = open('hw.csv')
    height = 0
    weight = 0
    p = []
    for line in a:
        y = line.replace(',', '')
        y1 = y.replace('"', '')
        y2 = y1.split()
        p.append(y2)
        try:
            height += float(y2[1])
            weight += float(y2[2])
            a1 = int(y2[0])
        except ValueError:
            pass
    avr_weight = round((weight / a1) / 2.205, 2)
    avr_height = round((height / a1) * 2.54, 2)

    return f'<h2>Средний вес: {avr_height} см., средний рост: {avr_weight} кг.</h2'


@app.route('/requirements')
def get_requirements():
    p = []
    f = open('requirements.txt')
    for line in f:
        p.append(line)
    l = '<br>'.join(p)
    return l


@app.route('/random_students')
def get_random_students():
    f = Faker()
    p = [f.name() for _ in range(100)]
    s = '<br>'.join(p)
    return s


app.run(debug=True)
