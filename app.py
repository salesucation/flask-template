from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)

@app.route("/")
def index():
    page = pages.get_or_404("index")
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    # Show the 10 most recent articles, most recent first.
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    return render_template('index.html', articles=latest[:10], page=page)

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'article.html')
    return render_template(template, page=page)
