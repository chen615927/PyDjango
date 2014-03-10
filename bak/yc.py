#coding = utf-8
import json
import MySQLdb
import MySQLdb.cursors

__author__ = 'chen jian ping'
__chen = 'pingping'

def Ptest():
    dic = {'name': 'chen', 'age': 32, 'addr': 'Bei Jing Chao Yan'}
    for k, v in dic.items():
        print k, 'aaa', v


def c():
    dic = {'name': 'chen jian ping', 'age': 32, 'addr': 'Bei Jing Chao Yang'}
    str = json.dumps(dic, sort_keys=True, indent = 4)
    print str
    di = json.loads(str)
    print type(di)
    print di['name']

def rf():
    fp = open('a.json', 'r')
    str = fp.read()
    dic = json.loads(str)
    for k, v in dic.items():
        for dic in v:
            for k1, v1 in dic.items():
                print k1,'-',v1

def dbs():
    conn=MySQLdb.connect(host='192.168.1.221',user='telephone',passwd='telephone_shopping',db='phpmall',port=3306, charset='utf8');
    cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    count = cur.execute('select * from mall_profile')
    print 'count is: %s' % count
    result = cur.fetchall()
    # print result
    # exit(0)
    for item in result:
      if item['nick_name']:
        print item['nick_name']
    cur.close()
    conn.close()
