import sqlite3


user_input = input("请输入用户名: ")


malicious_input = f"' OR 1=1--"


conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()


query = f"SELECT * FROM users WHERE username = '{user_input}' AND password = '{malicious_input}'"
query1 = f"select * FROM users WHERE username = '{user_input}' AND password = '{malicious_input}'"
cursor.execute(query)


result = cursor.fetchone()
if result:
    print("成功登录！")
else:
    print("登录失败！")


conn.close()
import sqlite3


user_input = input("请输入用户名: ")


malicious_input = f"' OR 1=1--"


conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()


query = f"SELECT * FROM users WHERE username = '{user_input}' AND password = '{malicious_input}'"
cursor.execute(query)

# 检查是否存在匹配的行
result = cursor.fetchone()
if result:
    print("成功登录！")
else:
    print("登录失败！")

# 关闭数据库连接
conn.close()