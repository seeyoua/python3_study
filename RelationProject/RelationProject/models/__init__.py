from .course import Course
from .grade import Grade
from .student import Student
from .users import Users

__all__ = [
    'Course',
    'Grade',
    'Student',
    'Users'
]

MODELS = __all__