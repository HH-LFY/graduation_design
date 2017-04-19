# -*- conding:utf-8 -*-

import logging

from tornado import *
from base.base_handler import BaseHandler as BaseHandler

class ManageLoginHandler(BaseHandler):
    def get(self):
        self.render('manage/login.html')

class ManageUserHandler(BaseHandler):

    def get(self):
        self.render('manage/user.html')

class ManageImgHandler(BaseHandler):
    def get(self):
        self.render('manage/image.html')

class ManageCategoryHandler(BaseHandler):
    def get(self):
        self.render('manage/category.html')
