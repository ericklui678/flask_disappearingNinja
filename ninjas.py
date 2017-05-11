from flask import Flask, render_template, request, redirect
app = Flask(__name__)

BLUE = 'blue'
ORANGE = 'orange'
RED = 'red'
PURPLE = 'purple'

@app.route('/')
def landingPage():
    return "No ninjas here"

@app.route('/ninja/<color>/')
def ninjaBlue(color):
    image = None
    if color == BLUE:
        image = 'leonardo.jpg'
    if color == ORANGE:
        image = 'michelangelo.jpg'
    if color == RED:
        image = 'raphael.jpg'
    if color == PURPLE:
        image = 'donatello.jpg'
    return render_template("index.html", dispImg=image or 'notapril.jpg')

@app.route('/ninjas')
def ninjas():
    return render_template("index.html", dispImg='tmnt.png')

app.run(debug = True)
