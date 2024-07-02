from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from urllib.parse import urlparse
import os


app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)

@app.route("/")
def index():
    page = pages.get_or_404("index")
    languages = os.listdir("pages")
    return render_template('index.html', page=page, languages=languages)

@app.route('/<path:path>')
def page(path):
    aParts = path.split("/")
    lang = aParts[0]
    page = pages.get(path, pages.get(f"{path}/index"))
    template = page.meta.get('template', f'{lang}/article.html')
    if "index" in template:
        # Articles are pages with a publication date
        articles = (p for p in pages if 'published' in p.meta and lang in p.path)
        # Show the 10 most recent articles, most recent first.
        latest = sorted(articles, reverse=True,
                        key=lambda p: p.meta['published'])
        languages = os.listdir("pages")
        return render_template(template, articles=latest[:10], page=page, languages=languages)
    else:
        return render_template(template, page=page)
