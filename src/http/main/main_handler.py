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

class ErrorHandler(BaseHandler):
    def get(self):
        self.render('error.html')


