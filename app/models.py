import flask_sqlalchemy, pytz
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model):
    __tablename__="xuser"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_Name=db.Column(db.String(30))
    user_Email=db.Column(db.String(256))
    password=db.Column(db.String(256))
    platform=db.Column(db.String(6))

    def __init__(self, user_Name, user_Email, password, platform) :
        self.user_Name = user_Name
        self.user_Email = user_Email
        self.password = password
        self.platform = platform



class Board(db.Model):
    now_utc = datetime.utcnow()
    seoul_timezone = pytz.timezone('Asia/Seoul')
    now_seoul = now_utc.replace(tzinfo=pytz.utc).astimezone(seoul_timezone)
    __tablename__="xboard"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    creator_id=db.Column(db.Integer)
    title=db.Column(db.String(40))
    content=db.Column(db.String(1000))
    location=db.Column(db.String(30))
    address=db.Column(db.String(50))
    recomend_up=db.Column(db.Integer, default=0)
    recomend_down=db.Column(db.Integer, default=0)
    created_at=db.Column(db.DateTime, default=now_seoul.now())
    delete_YN=db.Column(db.String(1), default='N')
    img_uid= db.Column(db.String(256), default='')
    def __init__(self, creator_id, title, content, location, address, img_uid):
        now_utc = datetime.utcnow()
        seoul_timezone = pytz.timezone('Asia/Seoul')
        now_seoul = now_utc.replace(tzinfo=pytz.utc).astimezone(seoul_timezone)
        self.creator_id = creator_id
        self.title = title
        self.content = content
        self.location = location
        self.address = address
        self.created_at = now_seoul.now()
        self.img_uid = img_uid


class recommand(db.Model):
    __tablename__="xrecommand"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    creator_id=db.Column(db.Integer)
    item_id=db.Column(db.Integer)
    item_type=db.Column(db.String(4))

    def __init__(self, creator_id, item_id, item_type):
        self.creator_id = creator_id
        self.item_id = item_id
        self.item_type = item_type

class festivalInfo(db.Model):
    __tablename__="xfestivalInfo"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title=db.Column(db.String(256))
    tel=db.Column(db.String(128))
    addr1=db.Column(db.String(64))
    addr2=db.Column(db.String(64))
    event_start_date=db.Column(db.String(8))
    event_end_date=db.Column(db.String(8))
    mapx=db.Column(db.String(40))
    mapy=db.Column(db.String(40))
    first_image=db.Column(db.String(512))

    def __init__(self, title, tel, addr1, addr2, event_start_date, event_end_date, mapx, mapy, first_image):
        self.title = title
        self.tel = tel
        self.addr1 = addr1
        self.addr2 = addr2
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.mapx = mapx
        self.mapy = mapy
        self.first_image = first_image
    