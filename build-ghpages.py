from flask_frozen import Freezer
from app import app

app.config.FREEZER_BASE_URL = "https://salesucation.github.io"
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()