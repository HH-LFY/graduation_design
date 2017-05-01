# -*- coding:utf-8 -*-

import logging
import threading

from manage_const import *
from tornado import *
from base.base_handler import *
from manage.manage_db import manage_db

class ManageLoginHandler(BaseHandler):

    @web.asynchronous
    def post(self):
        t = threading.Thread(target=self.doPost)
        t.start()

    def doPost(self):
        admin_username = self.get_argument('admin_name',None)
        password = self.get_argument('admin_password',None)
        param = [admin_username]
        ret = manage_db.getAdminInfoByAdminname(param)
        password = self.get_md5(password)
        if ret and password == ret.get('admin_password',None):
            self.set_secure_cookie('admin_username',admin_username)
            self.set_secure_cookie('admin_nickname',ret.get('admin_nickname',None))
            logging.info('admin_username:%s is login in .',admin_username)
            self.redirect('/manage/user_manage.html')
        else:
            logging.info('admin_username:%s is login error ,admin_username or password is error .',admin_username)
            self.make_render_admin('manage/login.html',
                            code = ERROR_FOR_ADMINNAME_PASSWORD,
                            code_msg = CODE_MSG[ERROR_FOR_ADMINNAME_PASSWORD])

    def get(self):
        self.make_render_admin('manage/login.html')

class ManageLoginOutHandler(BaseHandler):

    @auth_admin
    def get(self):
        self.clear_cookie('admin_username')
        self.clear_cookie('admin_nickname')
        self.redirect('/')


class ManageUserHandler(BaseHandler):

    @auth_admin
    def get(self):
        logging.info('get user_manage')
        users = manage_db.getAllUserInfo([0,INFO_LIST_COUNT])
        result = {
            'users':users,
        }
        self.make_render_admin('manage/user.html',
                                result=result)

class ManageImgHandler(BaseHandler):

    @auth_admin
    def get(self):
        self.make_render_admin('manage/image.html')

class ManageCategoryHandler(BaseHandler):

    @auth_admin
    def get(self):
        self.make_render_admin('manage/category.html')
