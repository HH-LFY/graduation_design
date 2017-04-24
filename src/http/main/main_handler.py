# -*- conding:utf-8 -*-

import logging
import time
import threading

from tornado import *
from main_const import *
from base.base_handler import BaseHandler as BaseHandler
from main.main_db import main_db




class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

class CategoryHandler(BaseHandler):

    def get(self):
        self.render('category.html')

class ImageDetailHandler(BaseHandler):
    def get(self):
        self.render('image_detail.html')

class PersonalInfoHandler(BaseHandler):
    def get(self):
        self.render('personal_info.html')

class ErrorHandler(BaseHandler):
    def get(self):
        self.render('error.html')

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

class RegisterHandler(BaseHandler):

    @web.asynchronous
    def post(self):
        t = threading.Thread(target=self.doPost)
        t.start()

    def doPost(self):
        logging.info('-------%s start-------',__name__)
        logging.info(main_db.insertUser())
        self.redirect('login.html')

    def get(self):
        self.render('register.html')