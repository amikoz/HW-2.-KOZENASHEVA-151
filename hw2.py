from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')

def mainpage():
    if request.args:
        f = open('data.json', 'a', encoding='utf-8') 
        s = json.dumps(request.args, f, ensure_ascii = False)
        f.write(s + '\n')
        f.close()
    return render_template('hello.html')

@app.route('/json')

def data():
    m = open('data.json', 'r', encoding='utf-8')
    data1 = []
    for line in m:
        data1.append(json.loads(line))
    return render_template('data.html', m=data1)

@app.route('/stats')

def statistic():
    n = open('data.json', 'r', encoding='utf-8')
    data2 = []
    for line1 in n:
        data2.append(json.loads(line1))
    return render_template('statistic.html', n=data2)

@app.route('/search')

def search():
    p = open('data.json', 'r', encoding='utf-8')
    return render_template('search.html')

def main():
    mainpage()
    data()
    statistic()
    search()
    
if __name__ == '__main__':
    app.run(debug=True)
