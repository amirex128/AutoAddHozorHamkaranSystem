import requests
import json
import urllib.parse
from datetime import datetime
import jdatetime
from datetime import timedelta

# find add holiday from https://www.time.ir/
holidays_shamsi = [
    '1403/04/01',
    '1403/04/05',
    '1403/04/06',
    '1403/04/07',
    '1403/04/08',
    '1403/04/09',
    '1403/04/10',
    '1403/04/11',
    '1403/04/12',
    '1403/04/13',
    '1403/04/14',
    '1403/04/15',
    '1403/04/16',
    '1403/04/18',
    '1403/04/21',
    '1403/04/22',
    '1403/04/25',
    '1403/04/26',
    '1403/04/28',
    '1403/04/29',
]
# add start day and end day for current month
start_shamsi = jdatetime.date(1403, 4, 1)
end_shamsi = jdatetime.date(1403, 5, 1)

# Just get new cookie from request in this url : https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index%5D?board=AttendanceDataCorrectionRequestEdit
cookie = 'themename=blue; themename-ui=uicupertino; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FU426sN7DcJzcRT1VVnutoWHhoeo64Tc4%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX189YzHjX2uMv4wJYjAHJ6UpPVAlVRnl9uk%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2B0JeoAtY7KqNLH6njzzGamgIu2I6HD9TU%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B5Kwr1RC4hX68kYCNihpaYf%2BE%2FhOr%2FcAA%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX18ybOBqmIipaZyxZbENYQxWBXkVUQvl4AAXLoOdh5o%2FnoKZSNM05TLhn%2FwVi0KhPpzpFyyYRbBudw%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BnGF1%2FXkcO4Puknt4%2BFYeFOQCqyCr9pXY%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX19iB9Thm%2F%2Fj7zGwECquhUwpeD64cSP8Cbo%2BN%2B1Tq6fu6dYAfP0emlJAGy43IKvLUMWe9h8kSfKmdngZMe3CDBKir3UBdZ59FYNSsdqBLbDpplxMAyaO7L64GDHNur80EJym7YdfReEy%2F5XYYQBdMIPThnm6rpNCMN3QPVaw2OLR2vXaiM7V1l%2B7v41TONDxkbfIzKk39UCEqbyGgnykESRUes6%2FEHsGW2z7oIQJNdFRnZW3Buj832YOegQ0NxGwf6qeWoXmsomeAQ7FJ9OU2NBQrelk28R6YhmbQ5PBPPbzabJiz8%2FG0ozRS%2B7%2F17N9q3xPCd9swebbu3KNYmPwTcZBzrrFZBjVdAWIJ7%2B4ujTVzVo1JIckzybm; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BZMPnjZ5cMHU%2FpXzpkJbTIBa8UlElXhqW3KE8IFTq9a6C1c5suBMiyKzShDsO2q1Opte9kKKQE8%2BoYTsIPfzCCOoSU2QatHjItpo3Mn5qDBwVi7TrnAFAoO7sbYCxXa%2F1Keayag%2FIrew%3D%3D; ASP.NET_SessionId=tyxyj4wieau1hgp3l12xr2ih; Lang=fa-IR; sg-dummy=-; sg-hcmportal-SnappPortal=9c3c156a-9f3a-4bab-ac0e-66566a619880; SgPresentation=ED5DB32F5A79605238456BC48AA4DB64378E9F6294DC0C3ECB50FED9C9AA2668B5E7CFE4815124C181E6C0C6C9AEC3FBC6640D31F5562E65196621EA7486DB99984A2B34BBA95C913F10D22EA84B89212348E74EF58560D179C4DCFE5C6D46E3135728445B2DAD33138D2D6C28083E0CDEB7CFC7; lastUrl=/SnappPortal/snappportal/Core/Index]?board=AttendanceDataCorrectionRequestEdit'

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
        data=data_encoded,verify=False
    )

    print(response.text)
