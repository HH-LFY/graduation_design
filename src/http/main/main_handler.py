# -*- conding:utf-8 -*-

import logging

from tornado import *
from base.base_handler import BaseHandler as BaseHandler

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
    def get(self):
        self.render('register.html')
