from flask_frozen import Freezer
from flask import url_for, render_template_string
from app import app
from flask_flatpages import FlatPages
import os

freezer = Freezer(app)
pages = FlatPages(app)

if __name__ == '__main__':
    with app.app_context():
    #freezer.freeze()
        for page in pages:
            template = page.meta.get('template', 'article.html')
            sPage = render_template_string(template, page=page)
            os.makedirs(f"{os.getcwd()}/build/{page.path}")
            f = open(f"{os.getcwd()}/build/{page.path}/index.html", "a")
            f.write(sPage)
            f.close()