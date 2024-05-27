from flask import Flask, render_template, request
import jwt

SECRET_KEY = 'a6a3e20e894ea4398f6ffac8c2a1fd98e4092a069a68597550533d00bb1d92d0'


def getUserInfo():
    token = request.cookies.get('token')
    if token != None:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        name = None
        email = None
        id = None
        if payload['name']!=None:
            name = payload['name']
        if payload['email']!=None:
            email = payload['email']
        if payload['id']!=None:
            id = payload['id']
        userInfo = {'name' : name, 'email' : email, 'id' : id}
        return userInfo
    else :
        return {'name' : '', 'email' : '', 'id' : ''}
        
    

def logoutService():
    token = request.cookies.get('token')
        
    return render_template('index.html')