
from flaskblog import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):   #table
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),default="default.jpg",nullable=False)
    password=db.Column(db.String(60),nullable=False)
    posts= db.relationship('Post',backref='author',lazy=True)

    #post has a relation.backref is
    #backref is adding another colum to the post model.it allows us to use author to get user who created post.
    def __repr__(self):#how our obj are printed
        return f"User( '{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)# passing function as arg
    content= db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):#how our obj are printed
        return f"User('{self.title}','{self.date_posted}')"
