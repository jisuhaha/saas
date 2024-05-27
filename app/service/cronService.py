from app.database import *
from app.models import *
        

def festivalRegistService(festival_json_data):
    from app.project import app
    with app.app_context():
        delete_all_instance(festivalInfo)
        for data in festival_json_data:
            if( len(data["firstimage"])!=0 ):
                add_instance(festivalInfo, title=data["title"], tel=data["tel"], addr1=data["addr1"], addr2=data["addr2"], event_start_date=data["eventstartdate"], event_end_date = data["eventenddate"], mapx = data["mapx"], mapy = data["mapy"], first_image = data["firstimage"])