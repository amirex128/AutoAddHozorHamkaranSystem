import requests
import json
import urllib.parse
from datetime import datetime
import jdatetime
from datetime import timedelta

# find add holiday from https://www.time.ir/
holidays_shamsi = [
    '1403/08/01',
    '1403/08/02',
    '1403/08/03',
    '1403/08/04',
    '1403/08/05',
    '1403/08/10',
    '1403/08/11',
    '1403/08/13',
    '1403/08/14',
    '1403/08/17',
    '1403/08/18',
    '1403/08/24',
    '1403/08/25'
]
start_shamsi = jdatetime.date(1403, 8, 5)
end_shamsi = jdatetime.date(1403, 9, 1)
# curl 'https://attendance.snappfood.ir/SnappPortal/snappportal/Core/DoOperation%5D?board=MissionDocumentEdit' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-US,en-AU;q=0.9,en-GB;q=0.8,en;q=0.7' \
#   -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
#   -H 'cookie: themename=blue; themename-ui=uicupertino; ASP.NET_SessionId=ranjlyxkva5a05ngtiadm5iu; Lang=fa-IR; sg-dummy=-; rl_user_id=RudderEncrypt%3AU2FsdGVkX19bfVOXtb8nsxsIAJqrdkLtd7XZYa6hO%2Fc%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX19ceatdq8GgOX4GuQ2VQiSchDxoIId5GnY%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19FLJiMauYtJojmobz5MZxxsXO4GxXPuEU%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19CcA8dWVKsdTkaahBq9RJnhHCY%2FfebYJk%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FFdhcVpmutn3N6TzvS57AJekxwyERxLRlq3%2BHuPtjrMVmCNQCu7hSKfh0FK3%2BI8SlOUG1cWJNrqg%3D%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BYCOYbp0U6NAbo3d2ehQP9lHfn6Nu9RZg%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FCgfghyOQP623qdLTdYwUSHT12en0xb6s%3D; rl_session=RudderEncrypt%3AU2FsdGVkX1%2Bd2ek9V8bO%2Fwdu%2FJp3ukWb1yQVIGVJsh0SI1rznM2HRZJHV3KyYXwtou9L89LUgjNHnu10%2FsdcTn9Otcm4IGOupNWveliMz%2Ftaz7C0PqqQ5kdvYd0%2BOj5D4wvv51ZdWUCpGp%2F4YGdaYw%3D%3D; sg-hcmportal-SnappPortal=58c37cf7-37b8-45b8-91e4-6a1d905a5852; lastUrl=/SnappPortal/snappportal/Core/Index]?board=MissionDocumentList; SgPresentation=0815799BE3024D4BFB1516F3561E1344660A13CD06120CD06DF28FB66C51ECAE29AB9D3372764A73FB5DBF6CB35CB62637A44453E2473FE27154FB027DA58068D26D9C368A66E125F58BFF4BCAC52744E670B25C98A7D8865C5DD57B0429B7B2E6690B8404326A6362C0CA16FB4244DA5988E4559D293BA0B1D9431DCE296C03D814A7B5' \
#   -H 'dnt: 1' \
#   -H 'origin: https://attendance.snappfood.ir' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index%5D?board=MissionDocumentEdit' \
#   -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' \
#   -H 'x-requested-with: XMLHttpRequest' \
#   --data-raw 'key=sg-MissionDocumentEdit-ib0-ref9-idun&board=MissionDocumentEdit&guid=bb77c7b9-b1c7-4671-80c6-7ffb79f55509&requestData=%7B%22sg-MissionDocumentEdit-ib0-idun%22%3A%7B%22hiddenFields%22%3A%5B%5D%2C%22fields%22%3A%7B%22f0%22%3A%220%22%2C%22f1%22%3A%22%22%2C%22f2%22%3A%221%22%2C%22f3%22%3A%22%22%2C%22f4%22%3A%22%22%2C%22f5%22%3A%22%22%2C%22f6%22%3A%22%22%2C%22f7%22%3A%22%22%2C%22f8%22%3A%22%22%2C%22f9%22%3A%2211%2F06%2F2024+12%3A09%3A28%22%2C%22f10%22%3A%22%22%2C%22f11%22%3A%2201%2F01%2F0001+00%3A00%3A00%22%2C%22f12%22%3A%220%22%2C%22f13%22%3A%2201%2F01%2F0001+00%3A00%3A00%22%2C%22f14%22%3A%220%22%2C%22f15%22%3A%22%22%2C%22f16%22%3A%2211%2F06%2F2024+00%3A00%3A00%22%2C%22f17%22%3A%2211%2F06%2F2024+00%3A00%3A00%22%2C%22f18%22%3A%2200%3A00%22%2C%22f19%22%3A%2224%3A00%22%2C%22f20%22%3A%2224%3A00%22%2C%22f21%22%3A%220010000%22%2C%22f22%22%3A%22False%22%2C%22f23%22%3A%22False%22%2C%22f24%22%3A%22False%22%2C%22f25%22%3A%22%22%2C%22f26%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22f27%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22f28%22%3A%22%22%2C%22lb0-lb0-f0%22%3A%224170%22%2C%22lb0-lb0-f1%22%3A%221403%2F08%2F16%22%2C%22lb0-lb0-f2%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb0-f0%22%3A%225%22%2C%22lb0-lb1-lb0-lb0-lb0-f1%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb0-f2%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb0-f3%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb0-f4%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb0-f5%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb1-f0%22%3A%220%22%2C%22lb0-lb1-lb0-lb0-lb1-f3%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb1-f1%22%3A%221403%2F08%2F06%22%2C%22lb0-lb1-lb0-lb0-lb1-f2%22%3A%2210%3A00%22%2C%22lb0-lb1-lb0-lb0-lb1-f6%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb1-f4%22%3A%221403%2F08%2F06%22%2C%22lb0-lb1-lb0-lb0-lb1-f5%22%3A%2219%3A00%22%2C%22lb0-lb1-lb0-lb0-lb1-f9%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb1-f7%22%3A%221403%2F08%2F06%22%2C%22lb0-lb1-lb0-lb0-lb1-f8%22%3A%2219%3A00%22%2C%22lb0-lb1-lb0-lb0-lb1-f12%22%3A%22%22%2C%22lb0-lb1-lb0-lb0-lb1-f10%22%3A%221%22%2C%22lb0-lb1-lb0-lb0-lb1-f11%22%3A%220009%3A00%22%2C%22lb0-lb1-lb0-lb0-lb1-f13%22%3A%22%D8%AF%D9%88%D8%B1%DA%A9%D8%A7%D8%B1%DB%8C%22%2C%22lb0-lb1-lb0-lb1-f0%22%3A%22%22%2C%22lb0-lb1-lb1-f0%22%3A%22%22%7D%7D%7D'
# Just get new cookie from request in this url : https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index%5D?board=AttendanceDataCorrectionRequestEdit
cookie = 'themename=blue; themename-ui=uicupertino; ASP.NET_SessionId=ranjlyxkva5a05ngtiadm5iu; Lang=fa-IR; sg-dummy=-; rl_user_id=RudderEncrypt%3AU2FsdGVkX19bfVOXtb8nsxsIAJqrdkLtd7XZYa6hO%2Fc%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX19ceatdq8GgOX4GuQ2VQiSchDxoIId5GnY%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19FLJiMauYtJojmobz5MZxxsXO4GxXPuEU%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19CcA8dWVKsdTkaahBq9RJnhHCY%2FfebYJk%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FFdhcVpmutn3N6TzvS57AJekxwyERxLRlq3%2BHuPtjrMVmCNQCu7hSKfh0FK3%2BI8SlOUG1cWJNrqg%3D%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BYCOYbp0U6NAbo3d2ehQP9lHfn6Nu9RZg%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2FCgfghyOQP623qdLTdYwUSHT12en0xb6s%3D; rl_session=RudderEncrypt%3AU2FsdGVkX1%2Bd2ek9V8bO%2Fwdu%2FJp3ukWb1yQVIGVJsh0SI1rznM2HRZJHV3KyYXwtou9L89LUgjNHnu10%2FsdcTn9Otcm4IGOupNWveliMz%2Ftaz7C0PqqQ5kdvYd0%2BOj5D4wvv51ZdWUCpGp%2F4YGdaYw%3D%3D; sg-hcmportal-SnappPortal=58c37cf7-37b8-45b8-91e4-6a1d905a5852; lastUrl=/SnappPortal/snappportal/Core/Index]?board=MissionDocumentList; SgPresentation=0815799BE3024D4BFB1516F3561E1344660A13CD06120CD06DF28FB66C51ECAE29AB9D3372764A73FB5DBF6CB35CB62637A44453E2473FE27154FB027DA58068D26D9C368A66E125F58BFF4BCAC52744E670B25C98A7D8865C5DD57B0429B7B2E6690B8404326A6362C0CA16FB4244DA5988E4559D293BA0B1D9431DCE296C03D814A7B5'

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
    'referer': 'https://attendance.snappfood.ir/SnappPortal/snappportal/Core/Index%5D?board=MissionDocumentEdit',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
URL = 'https://attendance.snappfood.ir/SnappPortal/snappportal/Core/DoOperation%5D?board=MissionDocumentEdit'

for day in working_days_shamsi:
    data = {
        'key': 'sg-MissionDocumentEdit-ib0-ref9-idun',
        'board': 'MissionDocumentEdit',
        'guid': 'c9b97c20-fb9e-457a-a314-c08a0670b54a',
        'requestData': {
            "sg-MissionDocumentEdit-ib0-idun": {
                "hiddenFields": [],
                "fields": {
                    "f0": "0",
                    "f1": "",
                    "f2": "1",
                    "f3": "",
                    "f4": "",
                    "f5": "",
                    "f6": "",
                    "f7": "",
                    "f8": "",
                    "f9": now.strftime("%m/%d/%Y %H:%M:%S"),
                    "f10": "",
                    "f11": "01/01/0001 00:00:00",
                    "f12": "0",
                    "f13": "01/01/0001 00:00:00",
                    "f14": "0",
                    "f15": "",
                    "f16": day,
                    "f17": day,
                    "f18": "00:00",
                    "f19": "24:00",
                    "f20": "24:00",
                    "f21": "0010000",
                    "f22": "False",
                    "f23": "False",
                    "f24": "False",
                    "f25": "",
                    "f26": "00000000-0000-0000-0000-000000000000",
                    "f27": "00000000-0000-0000-0000-000000000000",
                    "f28": "",
                    "lb0-lb0-f0": "4170",
                    "lb0-lb0-f1": day,
                    "lb0-lb1-lb0-lb0-lb0-f0": "5",
                    "lb0-lb1-lb0-lb0-lb0-f1": "",
                    "lb0-lb1-lb0-lb0-lb0-f2": "",
                    "lb0-lb1-lb0-lb0-lb0-f3": "",
                    "lb0-lb1-lb0-lb0-lb0-f4": "",
                    "lb0-lb1-lb0-lb0-lb0-f5": "",
                    "lb0-lb1-lb0-lb0-lb1-f0": "20094",
                    "lb0-lb1-lb0-lb0-lb1-f1": day,
                    "lb0-lb1-lb0-lb0-lb1-f2": "10:00",
                    "lb0-lb1-lb0-lb0-lb1-f3": "",
                    "lb0-lb1-lb0-lb0-lb1-f4": day,
                    "lb0-lb1-lb0-lb0-lb1-f5": "19:00",
                    "lb0-lb1-lb0-lb0-lb1-f6": "",
                    "lb0-lb1-lb0-lb0-lb1-f7": day,
                    "lb0-lb1-lb0-lb0-lb1-f8": "19:00",
                    "lb0-lb1-lb0-lb0-lb1-f9": "",
                    "lb0-lb1-lb0-lb0-lb1-f10": "1",
                    "lb0-lb1-lb0-lb0-lb1-f11": "0009:00",
                    "lb0-lb1-lb0-lb0-lb1-f13": "دورکاری",
                    "lb0-lb1-lb0-lb1-f0": "",
                    "lb0-lb1-lb1-f0": ""
                }
            }
        }
    }

    data['requestData'] = json.dumps(data['requestData'])
    data_encoded = urllib.parse.urlencode(data)

    response = requests.post(
        URL,
        headers=headers,
        data=data_encoded,
        verify=True
    )

    print(response.text)
