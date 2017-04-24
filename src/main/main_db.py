# -*- conding:utf-8 -*-

import sys
import logging
import enviroment
from base.connection_pool_mysql import MysqlConnection

class MainDb(object):
    """docstring for MainDb"""
    def __init__(self):
        logging.info('-------%s start-------',__name__)
        self.db = MysqlConnection()

    def insertUser(self):
        logging.info('-------%s start-------',__name__)

    def test(self):
        return self.db

main_db = MainDb()