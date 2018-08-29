# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv

names = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    # 한글 써도 에러 노노함.
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    match = random.randrange(50,101)
    
    # names 라는 배열에 입력된 두 이름을 넣는다.
    names.append(name1)
    names.append(name2)
    
    # names.csv 파일을 만들어서 저장한다.
    f = open('names.csv','a+', encoding='utf-8')
    a = csv.writer(f)
    a.writerow([name1, name2])
    f.close()
    
    return render_template('result.html', name1=name1, name2=name2, match=match)
    
    
@app.route("/admin")
def admin():
    # names 에 들어가 있는 모든 이름을 출력
    f= open('name.csv','r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names)
    
#app.run(host='0.0.0.0', port='8080', debug=True)