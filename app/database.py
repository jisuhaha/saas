from .models import db
from .models import Board


def get_all(model):
    data = model.query.all()
    return data

def get_count_filter_by_delete_flag(model, delete_flag):
    data = model.query.filter_by(delete_YN=delete_flag).count()
    return data

def get_instance_by_id(model, id):
    data = model.query.filter_by(id=id).all()[0]
    return data
    
def get_User_instance_by_Email(model, userEmail):
    data = model.query.filter_by(user_Email=userEmail).all()
    return data

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()

def delete_all_instance(model):
    model.query.delete()
    commit_changes()

def edit_instance(model, id, **kwargs):
    instance = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()

def commit_changes():
    db.session.commit()

def get_board_list(model, pageNo, rowCnt, delete_YN):
    data = model.query.filter_by(delete_YN=delete_YN).order_by(Board.created_at.desc()).limit(rowCnt).offset( (pageNo-1) * rowCnt ).all()
    return data