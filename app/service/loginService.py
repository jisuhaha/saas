from flask import render_template, request, jsonify, make_response
from app.database import *
from app.models import User
import hashlib
import jwt
from datetime import timedelta,datetime
from app.service.mainPageService import getUserInfo

SECRET_KEY = 'a6a3e20e894ea4398f6ffac8c2a1fd98e4092a069a68597550533d00bb1d92d0'

def potalLogin():
    email = request.form['email']
    password = request.form['password']
    data = get_User_instance_by_Email(User, email)
    resultChk = 0    
    for user in data:
        if user.platform=='nade':
            findResult=user
            resultChk=1
            break
    if resultChk == 1:
        inputPasswd = hashlib.sha256(password.encode()).hexdigest()
        pwdCheck = inputPasswd == findResult.password
        if pwdCheck == 1:
            payload = {
        'id' : findResult.id,
        'email': findResult.user_Email,
        'name' : findResult.user_Name,
        'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 1)
    }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            response = make_response('{"status":"success","message":"로그인 성공"}')
            response.set_cookie('token',token, max_age=60*60)
            return response
        else:
            response = make_response('{"status":"failed","message":"비밀번호가 일치하지 않습니다."}')
            return response
    else:
        response = make_response('{"status":"failed","message":"등록된 회원이 존재하지 않습니다."}')
        return response




def kakaoLogin():
    platform = 'kakao'
    userEmail = request.form['userEmail']
    userName = request.form['userName']
    enc_password = hashlib.sha256(userEmail.encode())
    data = None
    try:
        data = get_User_instance_by_Email(User, userEmail)
    except IndexError:
        print('is not registry User')
    finally:
        if len(data) != 0 :
            print('Login Success page')
        else:
            print('registry KaKao User')
            add_instance(User, user_Name = userName, user_Email= userEmail, password = enc_password.hexdigest(), platform=platform)
            data = get_User_instance_by_Email(User, userEmail)
    payload = {
        'id' : data[0].id,
        'email': userEmail,
        'name' : userName,
        'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    response = make_response('save KAKAO token cookie')
    response.set_cookie('token',token, max_age=60*60)
    return response

def naverLogin():
    platform = 'naver'
    userEmail = request.form['userEmail']
    userName = request.form['userName']
    enc_password = hashlib.sha256(userEmail.encode())
    data = None
    try:
        data = get_User_instance_by_Email(User, userEmail)
    except IndexError:
        print('is not registry User')
    finally:
        if len(data) != 0 :
            print('Login Success page')
        else:
            print('registry KaKao User')
            add_instance(User, user_Name = userName, user_Email= userEmail, password = enc_password.hexdigest(), platform = platform)
            data = get_User_instance_by_Email(User, userEmail)
            print('user data : ', data)
    payload = {
        'id' : data[0].id,
        'email': userEmail,
        'name' : userName,
        'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    response = make_response('save NaverLogin token cookie')
    response.set_cookie('token',token, max_age=60*60)
    return response

def loginTopFrameService():
    userInfo = getUserInfo()
    return userInfo