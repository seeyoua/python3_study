from RelationProject import db

class Grade(db.Model):
    g_id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    g_name = db.Column(db.String(20))
    g_desc= db.Column(db.String(100))
    #backref 该属性会把级联的student属性信息查询出来
    #并赋值给backref的第一个参数即"grade",关联类(User)会自动添加一个动态属性grade
    students = db.relationship('Student',backref='grade',lazy=True)

    __tablename__ = 'grade'
    def __init__(self,name,desc):
        self.g_name = name
        self.g_desc = desc

    def __repr__(self):
        return '<Grade %r, %r, %r>' % (self.g_id, self.g_name, self.g_desc)


