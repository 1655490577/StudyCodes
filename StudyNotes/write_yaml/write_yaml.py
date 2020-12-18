import yaml
import pymysql
import os

db = pymysql.connect("192.168.30.214", "root", "123456", "supervisor-test", autocommit=True)
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute("SELECT id ,`name`,`password`,phone FROM sys_admin WHERE dic_name = '测试公司'")
data = cur.fetchall()
# print(data)
data2 = {"test": [[f"{data[0]['id']}", f"{data[0]['name']}", f"{data[0]['password']}", f"{data[0]['phone']}"],
                  [f"{data[1]['id']}", f"{data[1]['name']}", f"{data[1]['password']}", f"{data[1]['phone']}"],
                  [f"{data[2]['id']}", f"{data[2]['name']}", f"{data[2]['password']}", f"{data[2]['phone']}"],
                  [f"{data[3]['id']}", f"{data[3]['name']}", f"{data[3]['password']}", f"{data[3]['phone']}"],
                  [f"{data[4]['id']}", f"{data[4]['name']}", f"{data[4]['password']}", f"{data[4]['phone']}"]]}

file_path = os.path.dirname(__file__)+"/test.yml"
with open(file_path, "w+") as f:
    yaml.dump(data2, f)

with open(file_path, "r") as ab:
    a = yaml.safe_load(ab)
    print(a)

cur.close()
db.close()
