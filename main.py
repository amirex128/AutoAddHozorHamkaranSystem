import requests
import json
import urllib.parse
from datetime import datetime
import jdatetime
from datetime import timedelta

# find add holiday from https://www.time.ir/
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
# add start day and end day for current month
start_shamsi = jdatetime.date(1403, 3, 1)
end_shamsi = jdatetime.date(1403, 4, 1)

# Just get new cookie from request in this url : https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index%5D?board=AttendanceDataCorrectionRequestEdit
cookie = 'themename=blue; themename-ui=uicupertino; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FSIuCyjw3unFXTnBhmI5Grm79qitRRi%2Fk%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FKxLpZyx%2BqQTYAH7TFjUIEqomRAIG%2BySY%3D; _gcl_au=1.1.1942426364.1715780867; ASP.NET_SessionId=r22rrscfakamvw4hyueucsjl; Lang=fa-IR; sg-dummy=-; rl_group_id=RudderEncrypt%3AU2FsdGVkX18wJbRGtn2yc8nb4%2Bv6BTGW1pbTo7fFtnk%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2Bq4B48YSQ0FlSNQKe%2FUG1hbKPadZ3Qzbk%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B01MlGx6%2F8Olb3xW6VcFX7BAC%2FgkrNIo6PPvvYzY9hPY45lPYL5QLtn2QscBptbRPk%2FqcOoRuRfA%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX19h9Oc0a8erB0QTUjCNKOKPt03n0CMOKpE%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX19Ns9b9Tqv%2FdzmPuEar3t9slP3In1p%2F5bEVgfgXOdICIHoOJxdYpX30OvKsU9Y3M1QKFZSVDeHWEAMRr43QO6p7zbBTc8X09kANNyUmgAns22PMrIuWMHcXxeHtpP%2BvOdIeG%2Ft1hhRS2Qvbk%2BENSsdruAseYd6M89ch91DPsNE76PBjwv0PbS7SJfxvsSDYXHWgAFqT3ZM2ie1Yp5LLtXARMGzOmmyCxwSi2ShPWSgjBKaTKWIBLPIn4cSNEKSIDYQ9uMa4IZaurItiBATjbRAngFyTrvTF0mO6V8Hf2%2BAV%2F5fP3YYsECKJvzPdi8rrJbjiXMOBJeXWgA%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX18%2FKrY%2FWqpXzFgBpuFqkyUejVxJO2XoGRAQkk5N3NFotLxESFtdQWyA%2FMUcQDWAxDBJvMBJSieBOGW9s0kU%2FsZOX%2BTfRBsKwDJISPoCiI4fBq5RY0eNBO0nbKNhQxKWipw0GK1x9JvPVg%3D%3D; sg-hcmportal-SnappPortal=55b1c218-0c0f-4165-92ff-5ec0b680835f; SgPresentation=FC3B6A0B290ED368191BFD61642978CD07135B310DE54BADE6BABA0F0ABCF561CBCCF1474DE4D3331E1B8B43648A4AB40F8D4DA64BA68FCE715F2A34E7504FE0B4464198BC1E7FA26E1BCD1A9C37C7E7E47B258CD44BB8581BDB18A1781D7A43B061A35EE34EACC8C83AA6516CAE384CE4CF2FDC; lastUrl=/SnappPortal/snappportal/Core/Index]?board=AttendanceDataCorrectionRequestEdit'

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
