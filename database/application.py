import os
from flask import Flask
from fms import db
from many_to_many import db as mm, Page, Tag

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.sqlite3')

# Register ORM
db.init_app(app)

with app.app_context():
    mm.create_all()


@app.route("/")
def index():
    return "bismillah Database Operation"

@app.route("/m2m")
def m2m():
    home = Page(name="Home")
    about = Page(name="About")
    contact = Page(name="Contact")
    db.session.add_all([home, about, contact])
    db.session.commit()

    google = Tag(name="Google")
    yahoo = Tag(name="Yahoo")
    bing = Tag(name="Bing")
    db.session.add_all([google, yahoo, bing])
    db.session.commit()

    home.tags.extend([google, yahoo])
    db.session.add(home)
    db.session.commit()

    home.tags = [] # Removed Previous items and add new items
    home.tags.extend([google, bing])
    db.session.add(home)
    db.session.commit()

    return "M2M"


if __name__ == '__main__':
    app.run()
