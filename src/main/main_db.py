# -*- coding:utf-8 -*-

import os
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
            ret = self.db.executeOne(SQL_INSERT_USER,param)
            logging.info(ret)
            # self.db.end()
            if ret :
                return True
            else:
                return False
        except:
            logging.error('insert into user is error.',exc_info=True)
            return False
            # self.db.end(False)

    def insertImg(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            ret = self.db.executeOne(SQL_INSERT_IMG,param)
            logging.info(ret)
            if ret :
                return True
            else:
                return False
        except:
            logging.error('insert into img is error.',exc_info=True)
            return False

    def insertPraiseImg(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            ret = self.db.executeOne(SQL_INSERT_PRAISE_IMG,param)
            logging.info(ret)
            if ret :
                return True
            else:
                return False
        except:
            logging.error('insert into insertPraiseImg is error.',exc_info=True)
            return False

    def insertColletImg(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            ret = self.db.executeOne(SQL_INSERT_COLLET_IMG,param)
            logging.info(ret)
            if ret :
                return True
            else:
                return False
        except:
            logging.error('insert into insertColletImg is error.',exc_info=True)
            return False

    def getCountByNicknameOrUsername(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            row = self.db.getOne(SQL_GET_USER_BY_NICKNAME_OR_USERNAME,param)
            ret = row[0]
            # self.db.end()
            if ret:
                return False
            else:
                return True
        except :
            logging.error('get count by nickname or username from db is error.',exc_info=True)
            return True
            # self.db.end(False)

    def getUserInfoByUsername(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            row = self.db.getOne(SQL_GET_USER_PASSWORD_BY_USERNAME,param)
            if row:
                user_id,user_nickname,user_username,user_password,user_header,_,_ = row
                ret = {
                    'user_id':user_id,
                    'user_nickname':user_nickname,
                    'user_username':user_username,
                    'user_password':user_password,
                    'user_header':user_header
                }
            else:
                ret = None
            return ret
        except :
            logging.error('get user password by username:%s from db is error.',param[0],exc_info=True)
            return None

    def getAllImgByCategoryId(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQL_GET_ALL_IMG_INFO_BY_CATEGORY_ID,param)
            rets = []
            for row in rows:
                img_id, img_addr, img_addr_small, img_size, img_author_id ,img_category_id, img_pv_count, img_md5, _, _ = row
                ret = {
                    'img_id':img_id,
                    'img_addr':img_addr,
                    'img_addr_small':img_addr_small,
                    'img_size':img_size,
                    'img_author_id':img_author_id,
                    'img_category_id':img_category_id,
                    'img_pv_count':img_pv_count
                }
                rets.append(ret)
            return rets
        except :
            logging.error('get user info by admin from db is error.',exc_info=True)
            return []

    def getImgInfoByImgid(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            row = self.db.getOne(SQL_GET_IMG_BY_IMGID,param)
            if row:
                img_id, img_addr, img_addr_small, img_size, img_author_id ,img_category_id, img_pv_count, img_md5, _, _ = row
                ret = {
                    'img_id':img_id,
                    'img_addr':img_addr,
                    'img_addr_small':img_addr_small,
                    'img_size':img_size,
                    'img_author_id':img_author_id,
                    'img_category_id':img_category_id,
                    'img_pv_count':img_pv_count,
                    'img_name':os.path.split(img_addr)[1]
                }
            return ret
        except :
            logging.error('get user password by username:%s from db is error.',param[0],exc_info=True)
            return None

    def getImgInfoByDate(self):
        logging.info('-------%s start-------',__name__)
        try:
            rows = self.db.getAll(SQL_GET_IMG_BY_DATE)
            ret = []
            for row in rows:
                img_id, img_addr, img_addr_small, img_size, img_author_id ,img_category_id, img_pv_count, img_md5, _, _ = row
                item = {
                    'img_id':img_id,
                    'img_addr':img_addr,
                    'img_addr_small':img_addr_small,
                    'img_size':img_size,
                    'img_author_id':img_author_id,
                    'img_category_id':img_category_id,
                    'img_pv_count':img_pv_count
                }
                # 获取赞数
                x = self.db.getOne(SQL_GET_IMG_PRAISE_NUM,[img_id])
                if x:
                    item['praise_num'] = x[0]
                ret.append(item)
            return ret
        except :
            logging.error('getImgInfoByDate from db is error.',exc_info=True)
            return None
main_db = MainDb()