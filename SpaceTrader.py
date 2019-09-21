# import statements
from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm

# Creating a Flask object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd291fd59e221b9a3a13c13b3b5dbc9e'

# Creating a route (a welcome page)
@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# Creating a route (a configuration screen)
@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Configure attribute for characters
        value = form.selectDifficulty.data
        pilotSkill = form.allocatePilot.data
        engineerSkill = form.allocateEngineer.data
        merchantSkill = form.allocateMerchant.data
        fighterSkill = form.allocateFighter.data
        sum = int(pilotSkill) + int(engineerSkill) + int(merchantSkill) + int(fighterSkill)
        if value == 'easy':
            if sum <= 16:
                return redirect(url_for('easy'))
        if value == 'medium':
            if sum <= 12:
                return redirect(url_for('medium'))
        if value == 'hard':
            if sum <= 8:
                return redirect(url_for('hard'))
    else:
        return render_template('configuration.html', form=form)

# Creating a route (page for choosing easy)
@app.route('/easy')
def easy():
    return render_template('finalEasy.html')

# Creating a route (page for choosing medium)
@app.route('/medium')
def medium():
    return render_template('finalMedium.html')

# Creating a route (page for choosing hard)
@app.route('/hard')
def hard():
    return render_template('finalHard.html')

# Run the environment
if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
