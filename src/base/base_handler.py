# -*- conding:utf-8 -*-

import os
import sys
import logging
import time

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """all handlers's base"""

    def get_current_user(self):
        return self.get_secure_cookie("user_username")