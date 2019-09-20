from flask import Blueprint
from ..models import Grade

grad = Blueprint('grade',__name__,url_prefix='/api/grades')
