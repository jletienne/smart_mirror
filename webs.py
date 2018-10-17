from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
  app.debug = True
  app.run()