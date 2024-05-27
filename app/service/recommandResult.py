from flask import render_template, request
import requests, random, json
from app.service.mainPageService import getUserInfo
from app.database import *
from app.models import *


def recommandResultService():    
    radius = request.form['radius']
    contentTypeId = request.form['contentTypeId']
    userInfo = getUserInfo()
    print(userInfo)

    return render_template('recommandResult.html', radius = radius, contentTypeId = contentTypeId, userInfo = userInfo)


def recommandAPIResultService():
    longitude = request.form['longitude']
    latitude = request.form['latitude']
    radius = request.form['radius']

    contentTypeId = request.form['contentTypeId'].strip()
    OPEN_KEY = 'your_datago_APIKEY'
    SERVICE_IDS = ['12', '14', '15', '28', '39']
    
    if( contentTypeId == '0'):
        contentTypeId = SERVICE_IDS[random.randrange(0,5)]
    

    locationURL = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1?ServiceKey=' + OPEN_KEY + '&_type=json&contentTypeId=' + contentTypeId + '&mapX=' + longitude + '&mapY=' + latitude + '&radius=' + radius + '&listYN=Y&MobileOS=ETC&MobileApp=AppTest&arrange=A&numOfRows=1000&pageNo=1&arrange=O'
    locationResponse = requests.get(locationURL)
    try:
        location_json_data = locationResponse.json()
    except requests.exceptions.JSONDecodeError:
        return recommandAPIResultService()
    randNum = random.randrange(0,len(location_json_data["response"]["body"]["items"]["item"])-1 )
    contentID = location_json_data["response"]["body"]["items"]["item"][randNum]["contentid"]
    contentTypeId = location_json_data["response"]["body"]["items"]["item"][randNum]["contenttypeid"]
    

    detailURL = 'http://apis.data.go.kr/B551011/KorService1/detailCommon1?MobileOS=ETC&MobileApp=test&_type=json&contentId='+ contentID + '&contentTypeId=' + contentTypeId + '&defaultYN=Y&firstImageYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&serviceKey='+ OPEN_KEY 
    detailResponse = requests.get( detailURL )
    try:
        detail_json_data = detailResponse.json()["response"]["body"]["items"]["item"][0]
    except requests.exceptions.JSONDecodeError:
        detail_json_data = recommandAPIResultService()

    detailInfoURL = 'http://apis.data.go.kr/B551011/KorService1/detailIntro1?MobileOS=ETC&MobileApp=test&_type=json&contentId='+ contentID +'&contentTypeId=' + contentTypeId + '&serviceKey='+ OPEN_KEY
    detailInfoResponse = requests.get( detailInfoURL )
    try:
        detailInfo_json_data = detailInfoResponse.json()["response"]["body"]["items"]["item"][0]
    except requests.exceptions.JSONDecodeError:
        detailInfo_json_data = {"infocenterculture" : "", "usetimeculture":"", "infocenter" :"", "usetime": "", "infocenterculture": "", "sponsor1tel": "", "playtime" : "","infocenterleports":"", "usetimeleports": "",
                                "infocentershopping" : "", "opentime" : "", "infocenterfood" : "", "opentimefood" : ""}
    
    if(contentTypeId == '12'):
        json_data = {"title" : detail_json_data["title"], "homepage" : detail_json_data["homepage"], "firstimage" : detail_json_data["firstimage"], "addr1" : detail_json_data["addr1"],
                   "mapx" : detail_json_data["mapx"], "mapy" : detail_json_data["mapy"], "overview" : detail_json_data["overview"], 
                   "infocenter" : detailInfo_json_data["infocenter"], "usetime" : detailInfo_json_data["usetime"]
                   }
    if(contentTypeId == '14'):
        json_data = {"title" : detail_json_data["title"], "homepage" : detail_json_data["homepage"], "firstimage" : detail_json_data["firstimage"], "addr1" : detail_json_data["addr1"],
                   "mapx" : detail_json_data["mapx"], "mapy" : detail_json_data["mapy"], "overview" : detail_json_data["overview"], 
                   "infocenter" : detailInfo_json_data["infocenterculture"], "usetime" : detailInfo_json_data["usetimeculture"]
                   }
    if(contentTypeId == '15'):
        json_data = {"title" : detail_json_data["title"], "homepage" : detail_json_data["homepage"], "firstimage" : detail_json_data["firstimage"], "addr1" : detail_json_data["addr1"],
                   "mapx" : detail_json_data["mapx"], "mapy" : detail_json_data["mapy"], "overview" : detail_json_data["overview"], 
                   "infocenter" : detailInfo_json_data["sponsor1tel"], "usetime" : detailInfo_json_data["playtime"]
                   }
    if(contentTypeId == '28'):
        json_data = {"title" : detail_json_data["title"], "homepage" : detail_json_data["homepage"], "firstimage" : detail_json_data["firstimage"], "addr1" : detail_json_data["addr1"],
                   "mapx" : detail_json_data["mapx"], "mapy" : detail_json_data["mapy"], "overview" : detail_json_data["overview"], 
                   "infocenter" : detailInfo_json_data["infocenterleports"], "usetime" : detailInfo_json_data["usetimeleports"]
                   }
    elif(contentTypeId == '38'):
        json_data = {"title" : detail_json_data["title"], "homepage" : detail_json_data["homepage"], "firstimage" : detail_json_data["firstimage"], "addr1" : detail_json_data["addr1"],
                   "mapx" : detail_json_data["mapx"], "mapy" : detail_json_data["mapy"], "overview" : detail_json_data["overview"], 
                   "infocenter" : detailInfo_json_data["infocentershopping"], "usetime" : detailInfo_json_data["opentime"]
                   }
    elif(contentTypeId == '39'):
        json_data = {"title" : detail_json_data["title"], "homepage" : detail_json_data["homepage"], "firstimage" : detail_json_data["firstimage"], "addr1" : detail_json_data["addr1"],
                    "mapx" : detail_json_data["mapx"], "mapy" : detail_json_data["mapy"], "overview" : detail_json_data["overview"], 
                    "infocenter" : detailInfo_json_data["infocenterfood"], "usetime" : detailInfo_json_data["opentimefood"]
                    }


    navURL = 'https://naveropenapi.apigw.ntruss.com/map-direction-15/v1/driving?start='+ longitude + ','+ latitude + '&goal='+ detail_json_data["mapx"] + ','+ detail_json_data["mapy"] +'&option=trafast'
    headers = {'X-NCP-APIGW-API-KEY-ID': 'duuy3z7x9p', 'X-NCP-APIGW-API-KEY' : 'iz2jLq7mcDWIN4nvlTjc80wdg9tHqrVzp6SAynXl'}
    navResponse = requests.get( navURL, headers=headers, verify=False)
    detailInfo_json_data = navResponse.json()
    if(detailInfo_json_data["code"] == 0):
        json_data["taxiFare"] = detailInfo_json_data["route"]["trafast"][0]["summary"]["taxiFare"]
        json_data["path"] = detailInfo_json_data["route"]["trafast"][0]["path"]
        json_data["startx"] = longitude
        json_data["starty"] = latitude

    
    return json_data


def searchFestivalService():
    data = get_all(festivalInfo)
    random.shuffle(data)
    json_str='['
    
    for i in range(5):
        json_str += '{ \"title\" :\"'+data[i].title+'\",'+'\"first_image\":\"'+data[i].first_image +'\"}'
        if i!=4:
            json_str +=','
    json_str+=']'
    return json_str