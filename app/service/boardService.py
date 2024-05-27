from flask import render_template,request, Response, redirect,jsonify
from app.service.mainPageService import getUserInfo
from app.database import *
from app.models import *
import math, boto3, uuid, os, pytz, requests

AWS_S3_BUCKET_NAME = "your_S3_bucket"
SECRET_KEY = 'youtMadeSecurtKey'
OPEN_KEY = 'your_datago_APIKEY'
def s3_connection():
    '''
    s3 Connection생성
    '''
    try:
        s3 = boto3.client(
            service_name='s3',
            verify=False
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3
    
def s3_put_object(s3, bucket, filepath, access_key, fileType):
    '''
    s3 bucket에 지정 파일 업로드
    :param s3: 연결된 s3 객체(boto3 client)
    :param bucket: 버킷명
    :param filepath: 파일 위치
    :param access_key: 저장 파일명
    :return: 성공 시 True, 실패 시 False 반환
    '''
    try:
        if fileType == 'jpg' or fileType ==  'jpeg':
            s3.upload_file(filepath, bucket, access_key,ExtraArgs={'ContentType':'image/jpeg'})
        elif fileType == 'png':
            s3.upload_file(filepath, bucket, access_key,ExtraArgs={'ContentType':'image/png'})
            
    except Exception as e:
        print(e)
        return False
    return "SUCCESS"


def createBoardBusiness():
    '''
    보드생성 페이지 이동
    '''
    userInfo = getUserInfo()
    token = request.cookies.get('token')
    if token != None:
        return render_template('boardCreate.html', userInfo = userInfo)
    else :
        return redirect('/board')

def sendBoardForm():
    now_utc = datetime.utcnow()
    seoul_timezone = pytz.timezone('Asia/Seoul')
    now_seoul = now_utc.replace(tzinfo=pytz.utc).astimezone(seoul_timezone)
    today = now_seoul.today().strftime("%Y%m%d")
    '''
    보드생성에서 등록 시 
    '''
    userInfo = getUserInfo()
    id = userInfo.get('id')
    if userInfo.get('id') == None:
        return 'test fail'
    title = request.form['title']
    location = request.form['location']
    content = request.form['content']
    files = request.files.getlist("thumbnailFile[]")
    s3 = s3_connection()
    imgUid=''
    for thumbFile in files:
        uid = str(uuid.uuid1())
        fileName = thumbFile.filename
        fileName =  fileName.split('.')
        fileType = fileName[len(fileName)-1]
        accessType = ['jpg','jpeg','png']
        if fileType not in accessType:
            continue
        uid = today + '/'+ uid + '.' + fileType
        imgUid += uid +'|'
        s3.upload_fileobj(thumbFile, AWS_S3_BUCKET_NAME, uid)
        """ filePath = './temp/'+thumbFile.filename
        thumbFile.save(filePath)
        s3_put_object(s3, AWS_S3_BUCKET_NAME, filePath, uid, fileType )
        os.remove(filePath) """
    TOTALSEARCH_URL = 'http://apis.data.go.kr/B551011/KorService1/searchKeyword1?numOfRows=12&_type=json&pageNo=1&MobileOS=ETC&MobileApp=AppTest&ServiceKey=' + OPEN_KEY +'&listYN=Y&arrange=A&areaCode=&sigunguCode=&cat1=&cat2=&cat3=&keyword=' + location
    totalSearch_Response = requests.get( TOTALSEARCH_URL )
    address = ''
    try:
        address = totalSearch_Response.json()["response"]["body"]["items"]["item"][0]['addr1']
    except:
        address = '-'
    if len(imgUid)!=0 and imgUid.strip()[-1] == '|':
        imgUid = imgUid[:-1]
    add_instance(Board, creator_id = id, title = title, content= content, location = location, address = address, img_uid= imgUid)

    return redirect('/board')

def modifyBoardForm():
    today = datetime.today().strftime("%Y%m%d")
    '''
    게시글 수정에서 수정 시 
    '''
    userInfo = getUserInfo()
    user_id = userInfo.get('id')
    if userInfo.get('id') == None:
        return 'test fail'
    title = request.form['title']
    location = request.form['location']
    content = request.form['content']
    id = request.form['id']
    files = request.files.getlist("thumbnailFile[]")
    s3 = s3_connection()
    imgUid=''
    for thumbFile in files:
        uid = str(uuid.uuid1())
        fileName = thumbFile.filename
        fileName =  fileName.split('.')
        fileType = fileName[len(fileName)-1]
        fileNameSplit = fileName[0].split('/')
        if len(fileNameSplit)>1:
            thumbFile.filename=fileNameSplit[1]
        accessType = ['jpg','jpeg','png']
        if fileType not in accessType:
            continue
        uid = today + '/'+ uid + '.' + fileType
        imgUid += uid +'|'
        filePath = './temp/'+thumbFile.filename
        thumbFile.save(filePath)
        s3_put_object(s3, AWS_S3_BUCKET_NAME, filePath, uid, fileType )
        os.remove(filePath)
    TOTALSEARCH_URL = 'http://apis.data.go.kr/B551011/KorService1/searchKeyword1?numOfRows=12&_type=json&pageNo=1&MobileOS=ETC&MobileApp=AppTest&ServiceKey=' + OPEN_KEY +'&listYN=Y&arrange=A&areaCode=&sigunguCode=&cat1=&cat2=&cat3=&keyword=' + location
    totalSearch_Response = requests.get( TOTALSEARCH_URL )
    address = ''
    try:
        address = totalSearch_Response.json()["response"]["body"]["items"]["item"][0]['addr1']
    except:
        address = ''
    if len(imgUid)>0 and imgUid.strip()[-1] == '|':
        imgUid = imgUid[:-1]
    edit_instance(Board, id=id,creator_id = user_id, title = title, content= content, location = location, address = address, img_uid= imgUid)
    return redirect('/board')

def getBoardList():
    '''
    후기 게시판 조회
    '''
    userInfo = getUserInfo()
    pageNo = request.args.get('pageNo')
    rowCnt = request.args.get('rowCnt')
    if pageNo is None:
        pageNo=1
    if rowCnt is None:
        rowCnt=10
    pageNo = int(pageNo)
    rowCnt = int(rowCnt)
    data = get_board_list(Board,pageNo=pageNo, rowCnt=rowCnt, delete_YN='N')
    for searchData in data:
        if len(searchData.img_uid)!= 0:
            searchData.img_uid = 'your_bucket_endPoint' + searchData.img_uid.split('|')[0]
    dataMaxCnt = get_count_filter_by_delete_flag(Board, 'N')
    minPage = math.trunc( pageNo / 10 ) * 10 + 1
    maxPage = math.trunc( dataMaxCnt / rowCnt )
    if dataMaxCnt % rowCnt >0:
        maxPage+=1
    if maxPage > minPage+9:
        maxPage = minPage+9
    return render_template('board.html', userInfo = userInfo, data= data, minPage=minPage, maxPage = maxPage)

def getBoardData():
    '''
    게시글 정보
    '''
    userInfo = getUserInfo()
    id = request.args.get('contentID')
    if id is None:
        id=10
    data = get_instance_by_id(Board, id)
    if len(data.img_uid) !=0:
        uid = str(data.img_uid)
        uidArr= uid.split("|")
        index = 0
        for uidData in uidArr:
            uidArr[index] = 'your_S3_bucket_endPoint'+ uidData
            index+=1
        data.img_uid = uidArr
    isCreator = data.creator_id == userInfo['id']
    return render_template('boardData.html', userInfo = userInfo, data = data, isCreator=isCreator)

def boardBoardEditService():
    '''
    게시글 수정 이동
    '''
    userInfo = getUserInfo()
    id = request.form["contentID"]
    data = get_instance_by_id(Board, id)
    if data.creator_id == userInfo['id']:
        return render_template('boardEdit.html', userInfo = userInfo, data = data)
    else:
        return redirect('/board')
    
def boardContentEditService():
    '''
    게시글 수정
    '''
    userInfo = getUserInfo()
    id = request.form["contentID"]
    data = get_instance_by_id(Board, id)
    if data.creator_id == userInfo['id']:
        ret = {"status" :"success", "message" : "게시물 수정을 할 수 있습니다."}
        return jsonify(ret)
    else:
        ret = {"status" :"failed", "message" : "게시물 수정을 할 수 없습니다."}
        return jsonify(ret)

def boardContentDeleteService():
    '''
    게시글 삭제
    '''
    userInfo = getUserInfo()
    id = request.form["contentID"]
    data = get_instance_by_id(Board, id)
    if data.creator_id == userInfo['id']:
        edit_instance(Board, id, delete_YN='Y')
        ret = {"status" :"success", "message" : "게시물을 삭제하였습니다."}
        return jsonify(ret)
    else:
        ret = {"status" :"failed", "message" : "게시물 삭제에 실패했습니다."}
        return jsonify(ret)
