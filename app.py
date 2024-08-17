from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '6844'
toolbar = DebugToolbarExtension(app)
debug = DebugToolbarExtension

@app.route('/')
def run():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)

@app.route("/story")
def make_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
    
    
    