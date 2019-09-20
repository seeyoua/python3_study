from .rest_students import stu
from .res_course import cour
from .rest_grade import grad
from .auth import auth

BLUEPRINT_MODELS = [
    stu,
    cour,
    grad,
    auth
]