# -*- coding:utf-8 -*-

import os
import sys
import logging
import time
import hashlib

import tornado.web

from all_code import *

class BaseHandler(tornado.web.RequestHandler):
    """all handlers's base"""

    def get_current_user(self):
        return self.get_secure_cookie("user_username")

    def get_md5(self,kstr):
        if not kstr:
            kstr = ''
        kstr = kstr + SALT
        m = hashlib.md5()
        m.update(kstr)
        return m.hexdigest()

    def make_render(self,template_name,code=SUCCESS_CODE,code_msg=CODE_MSG[SUCCESS_CODE],result=None):
        user_nickname = self.get_secure_cookie("user_nickname",None)
        self.render(template_name,
                    code = code,
                    code_msg = code_msg,
                    result = result,
                    user_nickname=user_nickname)