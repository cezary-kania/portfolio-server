import json
from datetime import date as dt
from app import db
from flask_mail import Message

class VisitCtrModel(db.Model):
    
    __tablename__ = 'visit_counters'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(10), unique = True, nullable = False)
    visits = db.Column(db.Integer, default = 0)
    
    def init_in_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def new_visit_msg(date = dt.today()):
        return Message(
                subject=f'[Portfolio visit] - Website visited at {date}',
                recipients=["cezary.kaniaq@gmail.com"],
                body="New visit on portfolio website registered")
    @staticmethod
    def get_all_visits():
        all_visits = VisitCtrModel.query.all()
        return all_visits

    @staticmethod
    def get_visit_ctr_by_id(visit_ctr_id):
        visits_ctr = VisitCtrModel.query.filter_by(id = visit_ctr_id).first()
        return visits_ctr

    @staticmethod
    def get_visit_ctr_by_date(date):
        visits_ctr = VisitCtrModel.query.filter_by(date = date).first()
        return visits_ctr

    @staticmethod
    def delete_visit_ctr(visit_ctr_id):
        visits_ctr = VisitCtrModel.query.filter_by(id = visit_ctr_id).first()
        try:
            db.session.delete(visits_ctr)
            db.session.commit()
            return visits_ctr
        except:
            return None
    @staticmethod
    def delete_all_ctrs():
        all_visits = VisitCtrModel.query.all()
        VisitCtrModel.query.delete()
        db.session.commit()
        return all_visits
    @staticmethod
    def register_visit():
        today = dt.today()
        visits_ctr = VisitCtrModel.query.filter_by(date = today).first()
        if visits_ctr is None:
            visits_ctr = VisitCtrModel(date = today)
            visits_ctr.init_in_db()
        visits_ctr.visits += 1
        db.session.commit()
        return visits_ctr

    @staticmethod
    def Get_all_visits_from_file():
        with open('../data/appdata.json', 'r+') as json_file:
            appdata = json.load(json_file)
            return appdata
    @staticmethod
    def Add_new_visit_to_file(request) -> dict:
        with open('../data/appdata.json', 'r+') as json_file:
            appdata = json.load(json_file)
            visitCounter = appdata['visitCounter']
            today = str(dt.today())
            todayCounter = list(filter(lambda dailyCounter: (dailyCounter['date'] == today), visitCounter))
            if len(todayCounter) != 0:
                todayCounter = todayCounter[0]
                todayCounter['amount'] = str(1 + int(todayCounter['amount']))
            else:
                todayCounter = {'date' : today, 'amount' : '1'}
                visitCounter.append(todayCounter)
            json_file.seek(0)
            json.dump(appdata,json_file,indent=3)
            json_file.truncate()
            return todayCounter