# -*- coding:utf-8 -*-

import sys
import logging
import enviroment
from all_code import *
from base.connection_pool_mysql import MysqlConnection

class ManageDb(object):
    def __init__(self):
        logging.info('-------%s start-------',__name__)
        self.db = MysqlConnection()

    def getAdminInfoByAdminname(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            row = self.db.getOne(SQL_GET_ADMIN_INFO_BY_ADMINNAME,param)
            if row:
                admin_id,admin_nickname,admin_username,admin_password,_,_ = row
                ret = {
                    'admin_id':admin_id,
                    'admin_nickname':admin_nickname,
                    'admin_username':admin_username,
                    'admin_password':admin_password,
                }
            else:
                ret = None
            return ret
        except :
            logging.error('get admin info by admin_username:%s from db is error.',param[0],exc_info=True)
            return None

    def getAllUserInfo(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQT_GET_ALL_USER_INFO,param)
            rets = []
            for row in rows:
                user_id,user_nickname,user_username,user_password,_,_,_ = row
                ret = {
                    'user_id':user_id,
                    'user_nickname':user_nickname,
                    'user_username':user_username,
                    'user_password':user_password,
                }
                rets.append(ret)
            return rets
        except :
            logging.error('get admin info by admin_username:%s from db is error.',param[0],exc_info=True)
            return []

manage_db = ManageDb()