from flask import Flask, render_template, url_for, redirect
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
    if form.validate_on_submit():
        value = dict(form.choice.choices).get(form.choice.data)
        pilotSkill = form.allocatePilot.data
        engineerSkill = form.allocateEngineer.data
        merchantSkill = form.allocateMerchant.data
        fighterSkill = form.allocateFighter.data
        sum = pilotSkill + engineerSkill + merchantSkill + fighterSkill
        if value == 'Easy':
            if sum <= 16:
                return redirect(url_for('easy'))
        if value == 'Medium':
            if sum <= 12:
                return redirect(url_for('medium'))
        if value == 'Hard':
            if sum <= 8:
                return redirect(url_for('hard'))
    return render_template('configuration.html', form=form)


@app.route('/easy')
def easy():
    return render_template('finalEasy.html')


@app.route('/medium')
def medium():
    return render_template('finalMedium.html')


@app.route('/hard')
def hard():
    return render_template('finalHard.html')


if __name__ == '__main__':
    app.run(debug=True)
