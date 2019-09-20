import json
from flask import Blueprint,request
from flask import jsonify
from flask import abort
from ..models import Student
from .. import db

stu = Blueprint('student',__name__,url_prefix='/api/students')


@stu.route('/<stu_id>',methods=['GET'])
def get_stu(stu_id):
    resut_dict = {}
    qureyset = Student.query.get(stu_id)
    if qureyset is None:
        abort(status=403)
    resut_dict['stu_name'] = qureyset.s_name
    resut_dict['stu_age'] = qureyset.s_age
    resut_dict['stu_id'] = qureyset.s_id
    resut_dict['grade'] = qureyset.grade.g_name
    resut_dict['desc'] = qureyset.grade.g_desc
    course_list = []
    courses = qureyset.courses
    for course in courses:
        course_list.append(course.c_name)
    resut_dict['course_list'] = course_list
    return jsonify(resut_dict)


@stu.route('/stu_add',methods=['POST','GET'])
def stu_add():
    if request.method == 'POST':
        stu_data = json.loads(request.get_data(as_text=True))
        count = Student.query.filter_by(s_name=stu_data.get('s_name')).count()
        if count!=0:
            result_data = stu_data
            result_data['status'] = 200
            result_data['message'] = "student is alaready exiest"
            return jsonify(result_data)
        else:
            s_name = stu_data.get('s_name')
            s_age = stu_data.get('s_age')
            g_id = stu_data.get('g_id')
            try:
                Stu = Student(s_name,s_age,g_id)
                db.session.add(Stu)
                db.session.commit()
            except Exception as e:
                print(e)
                return jsonify({"status":502,'errormessge':'服务器错误'})

            return jsonify({'status':201})













