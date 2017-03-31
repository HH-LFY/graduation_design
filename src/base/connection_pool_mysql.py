# -*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import MySQLdb
import threading
import logging
from conf import *
from DBUtils.PooledDB import PooledDB


def is_running():
    logging.info('%s is running~' % __file__)
    logging.info(CONF)

class MysqlConnection(object):
    """ mysql连接池 """

    # 连接池对象
    __pool = None
    def __init__(self):
        self.conn = MysqlConnection.__getConn()
        self.cursor = self.conn.cursor

    @staticmethod
    def __getConn():
        if MysqlConnection.__pool is None:
            __pool = PooledDB(CONF['ks'],CONF['db_mysql'])
        return __pool.connection()

def test_main():
    print('%s is running' % sys.argv[0].split('.')[0])
    db = MySQLdb.connect(**CONF['db_mysql'])
    cur = db.cursor()
    ret = cur.execute('show tables;')
    print('ret_type:%s \nret:%s' % (type(ret),ret))
    print('cur_type:%s' % type(cur))
    print('cur:%s' % cur.fetchall().__str__())
    print('cur:%s' % type(cur))
    cur.close()
    db.close()

if __name__=="__main__":
    test_main()

