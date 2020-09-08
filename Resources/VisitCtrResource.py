from flask_restful import Resource, fields, marshal, request, abort
from flask_mail import Message 
import json
from datetime import date as dt 


visit_fields = {
    'id' : fields.Integer,
    'Date' : fields.String(attribute='date'),
    'Visits ' : fields.Integer(attribute='visits')
}

class VisitCtrListResource(Resource):
    def post(self):
        from Models.VisitCtrModel import VisitCtrModel
        from app import mail
        result = VisitCtrModel.register_visit()
        try:
            msg = VisitCtrModel.new_visit_msg()
            # mail.send(msg) SMTP NOT CONFIGURED JET
            pass
        except:
            pass
        
        return marshal(result, visit_fields,envelope='Visit counter'), 200
    def get(self):
        from Models.VisitCtrModel import VisitCtrModel
        date = request.args.get('date')
        if date is None:
            visit_counters = VisitCtrModel.get_all_visits()
            return {'Visit counters': marshal(visit_counters,visit_fields) }, 200
        result = VisitCtrModel.get_visit_ctr_by_date(date)
        if result is None:
            abort(404, message = 'Visit counter not found')
        return marshal(result, visit_fields, envelope='Visit counter'), 200
    def delete(self):
        from Models.VisitCtrModel import VisitCtrModel
        deleted_ctrs = VisitCtrModel.delete_all_ctrs()
        return {'message' : 'deleted all visit counters', 
                'deleted counters': marshal(deleted_ctrs, visit_fields)
            }, 200

class VisitCtrResource(Resource):
    def get(self, visitsCtr_id):
        from Models.VisitCtrModel import VisitCtrModel
        result = VisitCtrModel.get_visit_ctr_by_id(visitsCtr_id)
        if result is None:
            abort(404, message = 'Visit counter not found')
        return marshal(result, visit_fields), 200
    def delete(self, visitsCtr_id):
        from Models.VisitCtrModel import VisitCtrModel
        result = VisitCtrModel.delete_visit_ctr(visitsCtr_id)
        if result is None:
            abort(404, message = 'Visit counter not found')
        return marshal(result, visit_fields, envelope='deleted visit counter'), 200
