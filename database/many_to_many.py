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


association_table = db.Table('association', db.metadata,
    db.Column('left_id', db.Integer, db.ForeignKey('left.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('right.id'))
)


class Parent(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")


class Child(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, primary_key=True)
    parents = db.relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")