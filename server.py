from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def mission(name=None):

    return render_template('mission.html')


@app.route('/join')
def join(name=None):

    return render_template('join.html')

@app.route('/minecraft')
def minecraft(name=None):

    return render_template('minecraft.html')

@app.route('/team')
def team(name=None):

    return render_template('team.html')

@app.route('/faq')
def faq(name=None):

    return render_template('faq.html')

@app.route('/contact')
def contact(name=None):

    return render_template('contact.html')

@app.route('/rank')
def rank(name=None):

    return render_template('rank.html')

@app.route('/explore')
def explore(name=None):

    return render_template('explore.html')


if __name__ == '__main__':
   app.run(debug = True)
