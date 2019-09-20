from RelationProject import db

#辅助表 纪录学生表和课程表的多对多关系
sc = db.Table('sc',
              db.Column('s_id',db.Integer,db.ForeignKey('student.s_id'),primary_key=True),
              db.Column('c_id', db.Integer, db.ForeignKey('course.c_id'), primary_key=True)
              )

class Course(db.Model):

    c_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    c_name = db.Column(db.String(20))  # 课程名称
    #secondary 指定附表名称
    students = db.relationship('Student', secondary=sc, backref='courses')
    __tablename__ = 'course'

    def __init__(self,name):
        self.c_name = name

    def __repr__(self):
        return '<Course %r, %r >' % (self.c_id, self.c_name)


