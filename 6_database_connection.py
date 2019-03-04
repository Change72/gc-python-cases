import pymysql
import cx_Oracle
import psycopg2

def mysql_connection():
    conn = pymysql.connect(
        host='localhost',  # mysql服务器地址
        port=3306,  # 端口号
        user='root',  # 用户名
        passwd='root',  # 密码
        db='Test',  # 数据库名称
        # charset = 'utf-8'#连接编码，根据需要填写
    )
    cur = conn.cursor()  # 创建并返回游标
    sq1 = "select * from t WHERE btag = 'buy' limit 0,100"
    cur.execute(sq1)  # 执行一个数据库查询命令
    rows = cur.fetchall()  # 获取结果中的所有行
    conn.close()  # 关闭对象
    return rows


def oracle_connection():
    ip = "127.0.0.1"
    username = "root"
    password = "root"
    oracle_port = "1521"
    oracle_service = "********"
    conn = cx_Oracle.connect(username + "/" + password + "@" + ip + ":" + oracle_port + "/" + oracle_service)
    cur = conn.cursor()  # 获取cursor
    sql = "select * from FINSTOCK.PRO_INVEST_INFO WHERE id = 2"
    x = cur.execute(sql)  # 使用cursor进行各种操作
    index = cur.description
    rows = x.fetchone()
    print(rows)
    print(index)
    cur.close()  # 关闭cursor
    conn.close()  # 关闭连接
    return rows


def postgres_connection():
    # read info from database
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    sql = "SELECT date FROM calendars;"
    cur.execute(sql)
    rows = cur.fetchall()  # all rows in table
    conn.commit()
    cur.close()
    conn.close()
    return rows