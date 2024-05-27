from flask import render_template,request
from app.service.mainPageService import getUserInfo
from app.database import *
from app.models import *
import hashlib

def registryIndexService():
    userInfo =getUserInfo()
    return render_template('registry.html',userInfo=userInfo)

def registryUserService():
    email = request.form['user_Email']
    name = request.form['user_Name']
    password = request.form['password']
    data = get_User_instance_by_Email(User, userEmail=email)
    userExist = 0
    for user in data:
        if user.platform=='nade':
            userExist=1
            break
    
    if userExist == 1:
        return '{"status" : "failed", "message": "이미 존재하는 회원."}'
    else:
        enc_password = hashlib.sha256(password.encode())
        add_instance(User, user_Name = name, user_Email= email, password = enc_password.hexdigest(), platform='nade')
        return '{"status" : "successed", "message": "회원가입 성공."}'
