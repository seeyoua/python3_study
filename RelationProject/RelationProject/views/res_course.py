import json
from flask import Blueprint,jsonify,request,abort
from ..common.tools import login_required
from ..models import Course
from .. import db

cour = Blueprint('course',__name__,url_prefix='/api/courses')


@cour.route('/',methods=['GET'])
@login_required
def get_curors():
    course_list = Course.query.all()
    resut_courses = {}
    records = []
    for cur in course_list:
        records.append(cur.c_name)
    resut_courses['Records'] = records
    resut_courses['status'] = 200
    return jsonify(resut_courses)


@cour.route('/create',methods=['GET','POST'])
def add_course():
    cour_data = json.loads(request.get_data(as_text=True))

    count = Course.query.filter_by(c_name =cour_data.get('c_name')).count()
    resut = dict()
    if count!=0:
        resut['c_id'] = cour_data.get('c_id')
        resut['message'] = "课程已经存在"
        resut['status'] = 200
        return jsonify(resut)
    c_name = cour_data.get('c_name')
    try:
        db.session.Course(Course(c_name))
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({"status": 502, 'errormessge': '服务器错误'})
    return jsonify({'status':201})


@cour.route('/delete/<id>',methods=['DELETE'])
def cour_delete(id):

    count = Course.query.filter_by(c_id=id).count()
    result = {}
    if count==0:
        result['status'] = 200
        result['message'] = "课程不存在"
        return jsonify(result)
    try:
        cour = Course.query.get(id)
        db.session.delete(cour)
        db.session.commit()
    except Exception as e:
        print(e)
    return jsonify({'status':200})











