from fms import db

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
                )


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('pages', lazy=True))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
