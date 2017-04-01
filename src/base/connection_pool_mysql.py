# -*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import MySQLdb
import threading
import logging
from conf import *
from DBUtils.PooledDB import PooledDB

class MysqlConnection(object):
    """ mysql连接池 """

    # 连接池对象
    __pool = None
    def __init__(self):
        self.conn = MysqlConnection.__getConn()
        self.cursor = self.conn.cursor()

    @staticmethod
    def __getConn():
        if MysqlConnection.__pool is None:
            __pool = PooledDB(**CONF['db_mysql'])
            logging.info('create new MysqlConnection_pool.')

        logging.info('get connection from MysqlConnection_pool.')
        return __pool.connection()

    def getCursor(self):
        return self.cursor

    # 查询单条语句
    def  getOne(self,sql,param=None):
        if param is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql,param)
        return self.cursor.fetchone()

    # 查询多条语句
    def getAll(self,sql,param=None):
        if param is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql,param)
        return self.cursor.fetchall()

    # 执行一条语句
    def executeOne(self,sql,param=None):
        if param is None:
            count = self.cursor.execute(sql)
        else:
            count = self.cursor.execute(sql,param)
        return count

    # 执行多条语句
    # param: list[list]/tuple(tiple)
    def executeMany(self,sql,param=None):
        if param is None:
            count = self.cursor.executemany(sql)
        else:
            count = self.cursor.executemany(sql,param)
        return count

    # 结束执行，虽然默认会commit，但是如果开启了事务，那需要手动的commit
    def end(self,commit=True):
        if commit:
            self.conn.commit()
        else:
            self.conn.rollback()

    # 关闭连接，
    def dispose(self,need_rollback=False):
        if need_rollback == False:
            self.end()
        else:
            self.end(False)
        self.cursor.close()
        self.conn.close()
        logging.info('close current connection.')

def test_mysql():
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

def test_pooled():
    db = MysqlConnection()
    sql = 'show tables;'
    ret = db.getAll(sql)
    print(ret)
    sql = 'select * from sys_config'
    ret = db.getOne(sql)
    print(ret)
    db.dispose()

if __name__=="__main__":
    test_pooled()

