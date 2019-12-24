from flask import Flask
from flask import request
import datetime
import json
app = Flask(__name__)

programmerDay = 255
noDateError = 27
dateFormatError = 54

@app.route('/')
def name():
    if request.args.get('year', '').isdigit() == False:
        data = {
            "errorCode": noDateError,
            "dataMassage": "There is no date"
        }
    else:
        year = int(request.args.get('year', ''))
        if year > 9999 or year < 1000:
            data = {
                "errorCode": dateFormatError,
                "dataMassage": "error in date format"
            }
        else:
            date = datetime.datetime(year, 1, 1)
            date = date + datetime.timedelta(programmerDay)
            data = {
                "errorCode": 200,
                "dataMassage": str(date.day) + "/" + str(date.month) + "/" + str(date.year)
            }
    data_json = json.dumps(data)
    return data_json


if __name__ == '__main__':
    app.run(port=80)