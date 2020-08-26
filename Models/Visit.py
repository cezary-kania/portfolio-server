import json
from datetime import date

class Visit:
    @staticmethod
    def Get_all_visits():
        with open('appdata.json', 'r+') as json_file:
            appdata = json.load(json_file)
            return appdata
    @staticmethod
    def Add_new_visit(request) -> dict:
        with open('appdata.json', 'r+') as json_file:
            appdata = json.load(json_file)
            visitCounter = appdata['visitCounter']
            today = str(date.today())
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