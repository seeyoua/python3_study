import hashlib
from flask import url_for,redirect,session
from functools import wraps

def md5_pwd(password):
    m = hashlib.md5()
    m.update(password.encode(encoding='UTF-8'))
    md5_value = m.hexdigest()
    return md5_value

def login_required(view):
    @wraps(view)
    def wrapped_views(*args,**kwargs):
        print(session)
        if session.get('user_id') is None:
            return redirect(url_for('auth.login'))
        return view(*args,**kwargs)
    return wrapped_views



