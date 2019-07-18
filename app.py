from classifier import classification as cf
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    a = cf.PersianClassifier()
    a.run()
    model = a.report.split('\n')
    for ac in range(1, 6):
        model[ac] = model[ac].replace(' ', '   ')
    l = a.accuracy
    return render_template('result.html', model=model, l=l)

if __name__ == '__main__':
    app.run(port=8000, debug=True)