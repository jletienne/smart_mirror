from flask import Flask, render_template, request, redirect, url_for
from mirror_python_code.quotes import request_quote

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    quote=request_quote()
    return render_template('index.html', quote=quote)

@app.route('/mirror')
def mirror():
    quote=request_quote()
    return render_template('index.html', title = 'Mirror', quote=quote)

if __name__ == '__main__':
    app.debug = True
    app.run()
