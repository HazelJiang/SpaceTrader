from flask import Flask, render_template, url_for
from forms import RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd291fd59e221b9a3a13c13b3b5dbc9e'


@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    form = RegistrationForm()
    return render_template('configuration.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
