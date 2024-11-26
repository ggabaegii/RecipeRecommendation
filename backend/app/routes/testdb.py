import pymysql
from flask import Blueprint

#db
db = pymysql.connect(host='127.0.0.1', user='root', password='qwer1234', db='test_db', charset='utf8')
cursor = db.cursor()
cursor.execute('INSERT INTO recipes (name, ingredients,instructions) VALUES ("BULGOGI", "MEAT", "고기를 재워서 뭐시기 한다")')

db.commit()
db.close()