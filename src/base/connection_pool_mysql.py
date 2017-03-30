# -*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import MySQLdb
import threading
import logging

def is_running():
    print('%s is running~' % __file__)

if __name__=="__main__":
    print('%s is running' % sys.argv[0].split('.')[0])
    db = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='sys',port=3306)
    cur = db.cursor()
    ret = cur.execute('show tables;')
    print('ret_type:%s \nret:%s' % (type(ret),ret))
    print('cur_type:%s' % type(cur))
    print('cur:%s' % cur.fetchall().__str__())
    print('cur:%s' % type(cur))
    cur.close()

