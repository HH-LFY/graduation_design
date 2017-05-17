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
            return row
        except :
            logging.error('get user password by username:%s from db is error.',param[0],exc_info=True)
            return None

    def getAllImgByCategoryId(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            rows = self.db.getAll(SQL_GET_ALL_IMG_INFO_BY_CATEGORY_ID,param)
            ret = self.__getPraiseNum(rows)
            return ret
        except :
            logging.error('get user info by admin from db is error.',exc_info=True)
            return {}

    def getImgInfoByImgid(self,param):
        logging.info('-------%s start-------',__name__)
        logging.info('param:%s',param)
        try:
            row = self.db.getOne(SQL_GET_IMG_BY_IMGID,param)
            if row:
                img_addr = row['img_addr']
                row['img_name'] = os.path.split(img_addr)[1]
                self.db.executeOne(SQL_UPDATE_IMG_PV,[row['img_id']])
            return row
        except :
            logging.error('get user password by username:%s from db is error.',param[0],exc_info=True)
            return None

    def getImgInfoByDate(self):
        logging.info('-------%s start-------',__name__)
        try:
            rows = self.db.getAll(SQL_GET_IMG_BY_DATE)
            logging.debug(rows)
            ret = self.__getPraiseNum(rows)
            return ret
        except :
            logging.error('getImgInfoByDate from db is error.',exc_info=True)
            return None


    def getMonthMaxImg(self):
        logging.info('-------%s start-------',__name__)
        try:
            rows = self.db.getAll(SQL_GET_IMG_MAX_PRAISE_NUM)
            ret = []
            for k in rows:
                ret.append(k['img_id'])
            rows = self.db.getAllUseIn(SQL_GET_IMG_BY_MANY_IMGID,ret)
            ret = self.__getPraiseNum(rows)
            return rows
        except :
            logging.error('getMonthMaxImg from db is error.',exc_info=True)
            return None

    def getPvMaxIMg(self):
        logging.info('-------%s start-------',__name__)
        try:
            rows = self.db.getAll(SQL_GET_IMG_MAX_PV)
            ret = self.__getPraiseNum(rows)
            return rows
        except :
            logging.error('getPvMaxIMg from db is error.',exc_info=True)
            return None

    def __getPraiseNum(self,rows):
        ret = []
        for i in xrange(len(rows)):
            img_id = rows[i]['img_id']
            # logging.debug('img_id:%s',img_id)
            x = self.db.getOne(SQL_GET_IMG_PRAISE_NUM,[img_id])
            # logging.debug('x:%s',x)
            if x:
                rows[i]['praise_num'] = x['count(user_id)']
            ret.append(rows[i])
        return ret

    def getCategoryByCategoryId(self,param):
        logging.info('-------%s start-------',__name__)
        try:
            row = self.db.getOne(SQL_GET_CATEGORY_BY_CATEGORY_ID,param)
            return row
        except :
            logging.error('getCategoryByCategoryId from db is error.',exc_info=True)
            return None

    def getFeedImg(self):
        logging.info('-------%s start-------',__name__)
        try:
            row = self.db.getAll(SQL_GET_IMG_FOR_FEED)
            return row
        except :
            logging.error('getFeedImg from db is error.',exc_info=True)
            return None


main_db = MainDb()