from flask import Flask, render_template
from

app = Flask(__name__)


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/configuration')
def configuration():
    return render_template('configuration.html')
if __name__ == '__main__':
    app.run(debug=True)
