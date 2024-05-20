import requests
import json
import urllib.parse
from datetime import datetime
import jdatetime
from datetime import timedelta

holidays_shamsi = [
    '1403/03/03',
    '1403/03/04',
    '1403/03/10',
    '1403/03/11',
    '1403/03/14',
    '1403/03/15',
    '1403/03/17',
    '1403/03/18',
    '1403/03/24',
    '1403/03/25',
    '1403/03/28',
    '1403/03/31',
]
start_shamsi = jdatetime.date(1403, 1, 1)
end_shamsi = jdatetime.date(1403, 1, 20)
cookie = 'themename=blue; themename-ui=uicupertino; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FSIuCyjw3unFXTnBhmI5Grm79qitRRi%2Fk%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FKxLpZyx%2BqQTYAH7TFjUIEqomRAIG%2BySY%3D; _gcl_au=1.1.1942426364.1715780867; rl_user_id=RudderEncrypt%3AU2FsdGVkX19QklFfLDclnoHgf%2BvjlX8P%2BosyRlVZscY%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2FH0517sjOpb%2B%2FBQCKERKK121fiUN%2Bj7W8%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19stMutTQ6SZokbCmkYHHaSejaDh7tO%2Be8%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19uVH5XtmSNScnma1SaSSjninfCfLxf3%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19N9WGXYwV8vEU5kxnBV8kOLJxtZezl2Nzn04VMmeNcRH21SIGQmgfz6xIAWM1d0e19IL4SQjMPEg%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BSF3jwOCAyiLJtBMK78NYmOBdH4t33tj4CDHr9KVHgYBi1UJkcNMyBZykwkXSSTV0wSK5R0s%2F1PX1dBmOnsGrjHvLBHXOKmmFq5dpoWGVBEfacLwmyvO71M1FrgnAbpQVodbJBAALkpQ%3D%3D; ASP.NET_SessionId=r22rrscfakamvw4hyueucsjl; Lang=fa-IR; sg-dummy=-; sg-hcmportal-SnappPortal=f8d71ff3-0315-4e26-9629-1762a43a673e; lastUrl=/SnappPortal/snappportal/Core/Index]?board=AttendanceDataCorrectionRequestList; SgPresentation=F61141241205EB3406E91F6B85550E4E23A7740FBE5FC5B7C29DF87E10218B5FA8CE24300BCA665511D059A8A466E43888BC5B591C0CE00B59517EDF544CCA67274C140D47C08C44DA78460539D5A48C7166037E718C4ECF9C8AA84DC6712D3F270248E2C39F8FDD2C94110D4E0BEE9974F17A8B'

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
        data=data_encoded
    )

    print(response.text)
