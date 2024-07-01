from flask import Flask, render_template
from flask_flatpages import FlatPages
import pandas as pd
import pygal
from pygal.style import Style

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

@app.route("/status")
def status():
    page = pages.get_or_404("status")
    df = pd.read_csv('https://anvil.works/blog/img/plotting-in-python/uk-election-results.csv')

    custom_style = Style(
        colors=('#0343df', '#e50000', '#ffff14', '#929591'),
        font_family='Roboto,Helvetica,Arial,sans-serif',
        background='transparent',
        plot_background='transparent',
        label_font_size=14,
    )

    c = pygal.Bar(
        title="UK Election Results",
        style=custom_style,
        y_title='Seats',
        x_label_rotation=270,
        no_prefix=True
    )
    c.add('Conservative', df['conservative'])
    c.add('Labour', df['labour'])
    c.add('Liberal', df['liberal'])
    c.add('Others', df['others'])

    c.x_labels = df['year']
    # c.render_to_file('static/pygal.svg')
    graph_data = c.render(is_unicode=True)
    return render_template("status_page.html", page=page, graph_data=graph_data)

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'article.html')
    return render_template(template, page=page)
