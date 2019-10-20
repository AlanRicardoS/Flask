from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    def __init__(self, username, name, password, email):
        self.username = username
        self.password = password
        self.name = name
        self.email =email



    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    user = db.relationship('User', foreign_keys=True)
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    def __repr__(self):
        return '<Post %r>' % self.id

class Follow(db.Model):
    __tablename__="follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_follower = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', foreign_keys = user_id)
    follwer = db.relationship('User', foreign_keys = follwer_id)
