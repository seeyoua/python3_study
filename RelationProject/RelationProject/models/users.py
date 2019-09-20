from RelationProject import db


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    __tablename__ = 'users'



    def __init__(self,username,password):
        self.username = username
        self.password = password
    def __repr__(self): #输出显示方法
        return '<Student %r, %r, %r>' % (self.username)