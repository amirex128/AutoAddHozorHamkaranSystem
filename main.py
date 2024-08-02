import requests
import json
import urllib.parse
from datetime import datetime
import jdatetime
from datetime import timedelta

# find add holiday from https://www.time.ir/
holidays_shamsi = [
    '1403/05/04',
    '1403/05/05',
    '1403/05/11',
    '1403/05/12',
    '1403/05/18',
    '1403/05/19',
    '1403/05/25',
    '1403/05/26'
]
# add start day and end day for current month
start_shamsi = jdatetime.date(1403, 5, 1)
end_shamsi = jdatetime.date(1403, 6, 1)

# Just get new cookie from request in this url : https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index%5D?board=AttendanceDataCorrectionRequestEdit
cookie = ''

now = datetime.now()
holidays_gregorian = set(jdatetime.date(*map(int, holiday.split('/'))).togregorian() for holiday in holidays_shamsi)


def is_working_day(date):
    if date.weekday() == 4:
        return False
    if date in holidays_gregorian:
        return False
    return True


working_days_shamsi = []
current_date_shamsi = start_shamsi
while current_date_shamsi <= end_shamsi:
    current_date_gregorian = current_date_shamsi.togregorian()
    if is_working_day(current_date_gregorian):
        working_days_shamsi.append(current_date_shamsi.strftime('%Y/%m/%d'))
    current_date_shamsi += timedelta(days=1)

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en-AU;q=0.9,en-GB;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'dnt': '1',
    'origin': 'https://attendance.snappfood.ir',
    'priority': 'u=1, i',
    'referer': 'https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index]?board=AttendanceDataCorrectionRequestEdit',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
URL = 'https://attendance.snappfood.ir/SnappPortal/snappportal/Core/DoOperation%5D?board=AttendanceDataCorrectionRequestEdit?board=AttendanceDataCorrectionRequestEdit'

for day in working_days_shamsi:
    data = {
        'key': 'sg-AttendanceDataCorrectionRequestEdit-ib0-ref5-idun',
        'board': 'AttendanceDataCorrectionRequestEdit',
        'guid': '2db56be6-cd59-46a5-a06d-351aa63feeb7',
        'requestData': {
            "sg-AttendanceDataCorrectionRequestEdit-ib0-idun": {
                "hiddenFields": [],
                "fields": {
                    "f0": "0",
                    "f1": now.strftime("%m/%d/%Y %H:%M:%S"),
                    "f2": "0",
                    "f3": "",
                    "f4": "01/01/0001 00:00:00",
                    "f5": "0",
                    "f6": "01/01/0001 00:00:00",
                    "f7": "0",
                    "f8": "False",
                    "f9": "",
                    "f10": "00000000-0000-0000-0000-000000000000",
                    "f11": "00000000-0000-0000-0000-000000000000",
                    "f12": "",
                    "lb0-lb0-lb0-f0": "4170",
                    "lb0-lb0-lb0-f1": day,
                    "lb0-lb0-lb1-lb0-f0": "دورکاری",
                    "lb0-lb0-lb1-lb0-f1": day,
                    "lb0-lb0-lb1-lb1-f0": ""
                }
            },
            "sg-AttendanceDataCorrectionRequestEdit-ib0-ib12-ib0-idun": {
                "oldSelectedId": -3,
                "items": [
                    {
                        "id": -2,
                        "stt": "new",
                        "cell": ["10:00", "ورود", "حضور", "", "", "", "", "", "", "", ""],
                        "hidn": ["10:00", "1", "2", "", "", "", "", "", "", "", ""]
                    },
                    {
                        "id": -3,
                        "slt": True,
                        "stt": "new",
                        "cell": ["19:00", "خروج", "حضور", "", "", "", "", "", "", "", ""],
                        "hidn": ["19:00", "2", "2", "", "", "", "", "", "", "", ""],
                        "details": {}
                    }
                ],
                "checkedIds": {"-3": True},
                "headerFilters": []
            }
        }
    }

    data['requestData'] = json.dumps(data['requestData'])
    data_encoded = urllib.parse.urlencode(data)

    response = requests.post(
        URL,
        headers=headers,
        data=data_encoded,
        verify=False
    )

    print(response.text)
