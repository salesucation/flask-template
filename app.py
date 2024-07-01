from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from urllib.parse import urlparse
import os


app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)

def getLang():
    o = urlparse(request.base_url)
    aPotentialLanguage = o.hostname.split(".")[0]
    if os.path.exists(f"pages/{aPotentialLanguage}"):
        return aPotentialLanguage
    else:
        return app.config["DEFAULT_LANG"]




@app.route("/")
def index():
    page = pages.get_or_404(f"{getLang()}/index")
    # Articles are pages with a publication date
    articles = (p for p in pages if 'published' in p.meta)
    # Show the 10 most recent articles, most recent first.
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['published'])
    return render_template(f'{getLang()}/index.html', articles=latest[:10], page=page)

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(f"{getLang()}/{path}")
    template = page.meta.get('template', 'article.html')
    return render_template(template, page=page)
