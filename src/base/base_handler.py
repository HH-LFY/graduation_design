# -*- coding:utf-8 -*-

import os
import sys
import logging
import time
import hashlib

import tornado.web

from all_code import *
from manage.manage_db import manage_db

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

    def make_render(self,template_name,code=SUCCESS_CODE,code_msg=CODE_MSG[SUCCESS_CODE],result={}):
        user_nickname = self.get_secure_cookie("user_nickname",None)
        categorys = manage_db.getAllCategoryInfo([0,100])
        result['categorys'] = categorys
        self.render(template_name,
                    code = code,
                    code_msg = code_msg,
                    result = result,
                    user_nickname = user_nickname)

    # admin
    def get_admin_user(self):
        return self.get_secure_cookie("admin_username")

    def make_render_admin(self,template_name,code=SUCCESS_CODE,code_msg=CODE_MSG[SUCCESS_CODE],result={}):
        admin_nickname = self.get_admin_user()
        self.render(template_name,
                    code = code,
                    code_msg = code_msg,
                    result = result,
                    admin_nickname = admin_nickname)

    def make_redirect(self,url,code=SUCCESS_CODE,code_msg=CODE_MSG[SUCCESS_CODE]):
        alert_str = '''<script type="text/javascript">alert('错误代码：%s\\n错误原因：%s');</script>''' % (code,code_msg)
        redirect_str = '''<script type="text/javascript"> window.location.href='%s';</script>''' % url
        self.write(alert_str)
        self.write(redirect_str)
        self.finish()

# 验证管理员用户
def auth_admin(method):
    def _auth_admin(self):
        admin = self.get_secure_cookie("admin_username")
        if not admin:
            self.redirect('/manage_login.html')
        else:
            logging.info('%s is authed.',admin)
            return method(self)
    return _auth_admin