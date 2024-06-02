from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
pages = FlatPages(app)

@app.route("/")
def index():
    return render_template("index.html");

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'article.html')
    return render_template(template, page=page)
