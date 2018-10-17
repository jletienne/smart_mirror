from flask import Flask, render_template, request, redirect, url_for
from quotes import request_quote

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/mirror')
def mirror():
    quote=request_quote()
    return render_template('mirror.html', title = 'Mirror', quote=quote)

if __name__ == '__main__':
    app.debug = True
    app.run()
