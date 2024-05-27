from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app.service.recommandResult import *
from app.service.loginService import *
from app.service.mainPageService import getUserInfo, logoutService
from app.service.boardService import *
from app.service.cronService import *
from app.service.registryService import *
from . import init, database
from .models import User
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import pytz
from app.service.myPageService import *


#app = Flask(__name__)
app = init.create_app()

@app.before_request
def log_client_ip():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    app.logger.info(f"Client IP: {client_ip}")
    
def festivalRegist():
    OPEN_KEY = 'your_datago_APIKEY'
    from datetime import datetime,timedelta
    now = datetime.now()
    today = datetime.today().strftime("%Y%m%d")
    afterWeek = now + timedelta(days=7)
    afterWeek = afterWeek.strftime("%Y%m%d")
    searchFestivalURL = 'http://apis.data.go.kr/B551011/KorService1/searchFestival1?eventStartDate='+ today + '&eventEndDate=' + afterWeek+ '&arrange=O&_type=json&areaCode=&sigunguCode=&ServiceKey=' + OPEN_KEY + '&listYN=Y&MobileOS=ETC&MobileApp=AppTest&arrange=A&numOfRows=100&pageNo=1'
    festivalResponse = requests.get( searchFestivalURL )
    try:
        festival_json_data = festivalResponse.json()["response"]["body"]['items']['item']
    except requests.exceptions.JSONDecodeError:
        return festivalRegist()
    festivalRegistService(festival_json_data)
schedule = BackgroundScheduler(daemon=True, timezone='Asia/Seoul') 

#schedule.add_job(festivalRegist, 'interval', seconds=10) 
schedule.add_job(festivalRegist, 'cron', hour='06',minute='00') 
schedule.start()


@app.route('/')
def home():
    userInfo = getUserInfo()
    return render_template('index.html', userInfo = userInfo)

@app.route('/recommand')
def recommand():
    userInfo = getUserInfo()
    return render_template('recommand.html', userInfo = userInfo)

@app.route('/searchFestival', methods=['POST'])
def searchFestival():
    return searchFestivalService()

@app.route('/recommandResult', methods=['POST'] )
def recommandResult():
    return recommandResultService()


@app.route('/recommandAPIResult', methods=['POST'] )
def recommandAPIResult():
    return recommandAPIResultService()

@app.route('/registry')
def registryPage():
    return registryIndexService()

@app.route('/registryUser', methods=['POST'])
def user_registry():
    return registryUserService()

@app.route('/login')
def user_login():
    userInfo = getUserInfo()
    return render_template('login.html', userInfo = userInfo)

@app.route('/naverLoginCallback')
def naverLoginCallback():
    return render_template('naverLoginCallback.html')

@app.route('/kakaoLoginCallback')
def kakaoLoginCallback():
    return render_template('kakaoLoginCallback.html')

@app.route('/loginFromPortal', methods=['POST'] )
def loginFromPortal():
    return potalLogin()

@app.route('/loginFromKakao', methods=['POST'] )
def loginFromKakao():
    return kakaoLogin()

@app.route('/loginFromNaver', methods=['POST'] )
def loginFromNaver():
    return naverLogin()

@app.route('/loginTopFrame', methods=['POST'] )
def loginTopFrame():
    return loginTopFrameService()

@app.route('/board')
def board():
    return getBoardList()

@app.route('/boardCreate')
def boardCreate():
    return createBoardBusiness()


@app.route('/boardCreateService', methods=['POST'] )
def boardCreateService():
    return sendBoardForm()

@app.route('/boardModifyService', methods=['POST'])
def boardModifyService():
    return modifyBoardForm()

@app.route('/getBoardData')
def boardData():
    return getBoardData()

@app.route('/boardEdit', methods=['POST'] )
def boardBoardEdit():
    return boardBoardEditService()


@app.route('/contentEdit', methods=['POST'] )
def boardContentEdit():
    return boardContentEditService()

@app.route('/contentDelete', methods=['POST'] )
def boardContentDelete():
    return boardContentDeleteService()


@app.route('/myPage')
def myPage():
    return getMyPageService()

@app.route('/modifyUser', methods = ['POST'])
def modifyUser():
    return modifyUserService()