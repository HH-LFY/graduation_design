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

    # user
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
                    user_nickname = user_nickname)

    # admin
    def get_admin_user(self):
        return self.get_secure_cookie("admin_username")

    def make_render_admin(self,template_name,code=SUCCESS_CODE,code_msg=CODE_MSG[SUCCESS_CODE],result=None):
        admin_nickname = self.get_admin_user()
        self.render(template_name,
                    code = code,
                    code_msg = code_msg,
                    result = result,
                    admin_nickname = admin_nickname)

def auth_admin(method):
    def _auth_admin(self):
        admin = self.get_secure_cookie("admin_username")
        if not admin:
            self.redirect('/manage_login.html')
        else:
            logging.info('%s is authed.',admin)
            return method(self)
    return _auth_admin