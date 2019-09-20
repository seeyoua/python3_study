from flask import Blueprint,request,jsonify,session
from ..common.tools import md5_pwd
from ..models import Users
from .. import db
auth = Blueprint('auth',__name__,url_prefix='/api')



@auth.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is None:
            return jsonify({'errormessage':'请输入用户名'})
        if password is None:
            return jsonify({'errormessage':"请输入密码"})
        count = Users.query.filter_by(username=username).count()
        if count !=0:
            return jsonify({'status':200,'messages':'用户存在'})

        pwd = md5_pwd(password)
        try:
            db.session.add(Users(username,pwd))
            db.session.commit()
        except Exception as e:
            return jsonify({'status':502})
        return jsonify({'status':201,'messages':'注册成功'})


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form.get("username")
        password = request.form.get('password')
        count = Users.query.filter_by(username=username).count()

        if count==0:
            return jsonify({'status':200,'messages':'用户不存请注册'})
        if password is not None:
            value = md5_pwd(password)
            qurey_data = Users.query.filter_by(username=username).first()
            if qurey_data.password == value:
                session['user_id'] = qurey_data.id
                return jsonify({'status':200,'message':'登入成功'})
    return jsonify({'staus':200,'messages':'请重新登入'})







