from flask import Flask, render_template, request
from app.service.mainPageService import getUserInfo
from app.database import *
from app.models import *
import hashlib

def getMyPageService():
    userInfo = getUserInfo()
    return render_template('myPage.html', userInfo = userInfo)

def modifyUserService():
    userInfo = getUserInfo()
    password = request.form['password']
    userID = request.form['userID']
    enc_password = hashlib.sha256(password.encode())
    edit_instance(User, id= userID, password = enc_password.hexdigest())
    
    return '{"status" : "successed", "message": "개인정보 수정 성공."}'