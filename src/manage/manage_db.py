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
            return row
        except :
            logging.error('get admin info by admin from db is error.',param[0],exc_info=True)
            return None

    def getAllUserInfo(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQT_GET_ALL_USER_INFO,param)
            return rows
        except :
            logging.error('get user info by admin from db is error.',exc_info=True)
            return []

    def insertCategory(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            ret = self.db.executeOne(SQL_INSERT_CATEGORY,param)
            return ret
        except:
            logging.error('unknow reason execute sql in db is error.',exc_info=True)
            return False

    def getAllCategoryInfo(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQL_GET_ALL_CATEGORY_INFO,param)
            return rows
        except :
            logging.error('get category info by admin from db is error.',exc_info=True)
            return []

    def getAllImg(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQL_GET_ALL_IMG,param)
            ret = self.__getPraiseNumAndRecommend(rows)
            return rows
        except :
            logging.error('get category info by admin from db is error.',exc_info=True)
            return []

    def opImg(self,op,img_id):
        logging.info('-------%s start-------',__name__)
        try:
            ret = False
            if op=='del_img':
                ret = self.db.executeOne(SQL_DELETE_IMG_BY_IMGID,[img_id])
            elif op=='recommend_img':
                if self.db.getOne(SQL_GET_IMG_RECOMMEND,[img_id]) is None:
                    ret = self.db.executeOne(SQL_RECOMMEND_IMG_BY_IMGID,[img_id])
                else:
                    logging.error('the img already recommend_img.')
            elif op=='cancel_recommend_img':
                ret = self.db.executeOne(SQL_CANCEL_RECOMMEND_IMG_BY_IMGID,[img_id])
            return ret
        except:
            logging.error('unknow reason execute sql in db is error.',exc_info=True)
            return False

    def __getPraiseNumAndRecommend(self,rows):
        ret = []
        for i in xrange(len(rows)):
            img_id = rows[i]['img_id']
            x = self.db.getOne(SQL_GET_IMG_PRAISE_NUM,[img_id])
            if x:
                rows[i]['praise_num'] = x['count(user_id)']
            x = self.db.getOne(SQL_GET_IMG_RECOMMEND,[img_id])
            if x:
                rows[i]['recommend'] = bool(x['judge'])
            ret.append(rows[i])
        return ret

    def getAllDiscussInfo(self):
        logging.info('-------%s start-------',__name__)
        try:
            rows = self.db.getAll(SQL_GET_DISCUSS)
            return rows
        except :
            logging.error('get getAllDiscussInfo info by admin from db is error.',exc_info=True)
            return []

manage_db = ManageDb()