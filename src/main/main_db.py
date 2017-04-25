# -*- coding:utf-8 -*-

import sys
import logging
import enviroment
from all_code import *
from base.connection_pool_mysql import MysqlConnection

class MainDb(object):
    """docstring for MainDb"""
    def __init__(self):
        logging.info('-------%s start-------',__name__)
        self.db = MysqlConnection()

    def insertUser(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            ret = self.db.executeOne(INSERT_USER,param)
            logging.info(ret)
            # self.db.end()
            if ret :
                return True
            else:
                return False
        except:
            logging.error('insert into user is error.',exc_info=True)
            # self.db.end(False)

    def getCountByNicknameOrUsername(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            row = self.db.getOne(GET_USER_BY_NICKNAME_OR_USERNAME,param)
            ret = row[0]
            logging.info(ret)
            # self.db.end()
            if ret:
                return False
            else:
                return True
        except :
            logging.error('get count by nickname or username from db is error.',exc_info=True)
            # self.db.end(False)

main_db = MainDb()