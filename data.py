# 파이썬 dict 타입으로 공공데이터 다운 받기 (requests 모듈 사용)
# 다운 받은 데이터를 DB에 INSERT 하기
# http://openapi.seoul.go.kr:8088/5178646171736d6835394f45744953/json/RealtimeCityAir/1/5/

import requests
import pymysql

# MariaDB 연결하기
db = pymysql.connect(
    user='green',
    passwd='green1234',
    host='localhost',
    db='greendb',
    charset='utf8'
)

# 커서 획득
cursor = db.cursor()

# 공공데이터 url
url = 'http://openapi.seoul.go.kr:8088/5178646171736d6835394f45744953/json/RealtimeCityAir/1/25/'

# 공공데이터 response에 담기
response = requests.get(url)

jsonData = None  # json으로 담을 변수
# print(response.text)

data = None  # 필요한 데이터만 json으로 담을 변수

# http 상태코드가 200이면
if response.status_code == 200:
    # 공공데이터 json으로 받기
    jsonData = response.json()
    # print(jsonData.get("RealtimeCityAir").get("row"))

    # 필요한 데이터만 담기
    data = jsonData.get("RealtimeCityAir").get("row")
    # for d in data:
    #     print(d)

    # 데이터 insert - dict 형 데이터
    # INSERT INTO `테이블명` VALUES(...)으로 사용 시 컬럼 수가 맞아야 한다. (지금은 id 때문에 사용 못 함)
    sql = "INSERT INTO weather (msrdt, msrrgn_nm, msrste_nm, pm10, pm25, o3, no2, co, so2, idex_nm, idex_mvl, arplt_main) VALUES (%(MSRDT)s, %(MSRRGN_NM)s, %(MSRSTE_NM)s, %(PM10)s, %(PM25)s, %(O3)s, %(NO2)s, %(CO)s, %(SO2)s, %(IDEX_NM)s, %(IDEX_MVL)s, %(ARPLT_MAIN)s);"
    cursor.executemany(sql, data)
    db.commit()  # commit까지 해줘야 insert 완료 됨
