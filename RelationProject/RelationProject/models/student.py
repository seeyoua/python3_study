from RelationProject import db


class Student(db.Model):
    s_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name = db.Column(db.String(20))
    s_age = db.Column(db.Integer,default=20)
    g_id= db.Column(db.Integer,db.ForeignKey('grade.g_id'))

    __tablename__ = 'student'

    def __init__(self,name,age,g_id):
        self.s_name = name
        self.s_age = age
        self.g_id = g_id

    def __repr__(self): #输出显示方法
        return '<Student %r, %r, %r>' % (self.s_id, self.s_name, self.s_age)

