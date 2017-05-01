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
            logging.error('get admin info by admin from db is error.',param[0],exc_info=True)
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
            logging.error('get user info by admin from db is error.',exc_info=True)
            return []

    def insertCategory(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            ret = self.db.executeOne(SQL_INSERT_CATEGORY,param)
            if ret:
                return True
            else:
                return False
        except:
            logging.error('unknow reason execute sql in db is error.',exc_info=True)
            return False

    def getAllCategoryInfo(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQL_GET_ALL_CATEGORY_INFO,param)
            rets = []
            for row in rows:
                c_id,c_pid,c_name,c_remark,_ = row
                ret = {
                    'c_id':c_id,
                    'c_pid':c_pid,
                    'c_name':c_name,
                    'c_remark':c_remark
                }
                rets.append(ret)
            return rets
        except :
            logging.error('get category info by admin from db is error.',exc_info=True)
            return []

manage_db = ManageDb()