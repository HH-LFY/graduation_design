# -*- coding:utf-8 -*-

import logging
import time
import threading
import random


from all_code import *
from tornado import *
from main_const import *
from base.base_handler import BaseHandler
from main.main_db import main_db




class IndexHandler(BaseHandler):
    def get(self):
        self.make_render('index.html')

class CategoryHandler(BaseHandler):

    def get(self):
        self.make_render('category.html')

class ImageDetailHandler(BaseHandler):
    def get(self):
        self.make_render('image_detail.html')

class PersonalInfoHandler(BaseHandler):
    def get(self):
        self.make_render('personal_info.html')

class ErrorHandler(BaseHandler):
    def get(self):
        self.make_render('error.html')

class LoginHandler(BaseHandler):

    @web.asynchronous
    def post(self):
        t = threading.Thread(target=self.doPost)
        t.start()

    def doPost(self):
        logging.info('-------%s start-------',__name__)
        user_username = self.get_argument('username',None)
        password = self.get_argument('password',None)
        param = [user_username]
        ret = main_db.getUserInfoByUsername(param)
        password = self.get_md5(password)
        if ret and password == ret.get('user_password',None):
            self.set_secure_cookie('user_username',user_username)
            self.set_secure_cookie('user_nickname',ret.get('user_nickname',None))
            logging.info('user_username:%s is login in .',user_username)
            self.redirect('/')
        else:
            logging.info('user_username:%s is login error ,user_username or password is error .',user_username)
            self.make_render('login.html',
                            code = ERROR_CODE_FOR_USERNAME_PASSWORD,
                            code_msg = CODE_MSG[ERROR_CODE_FOR_USERNAME_PASSWORD])


    def get(self):
        self.make_render('login.html')

class LoginOutHandler(BaseHandler):

    @web.authenticated
    def get(self):
        logging.info('-------%s start-------',__name__)
        logging.info('user_username:%s is login out .',self.get_secure_cookie('user_username'))
        self.clear_cookie('user_username')
        self.clear_cookie('user_nickname')
        self.redirect('/')


class TestHandler(BaseHandler):
    def get(self):
        self.write('<html><a href="http://121.52.235.231:40030/page_v3/wallet_coin.html?_token=98890ded-3fc2-4f19-8d09-f68f1f9f9458">http://max_len1.52.235.231:40030/page_v3/wallet_coin.html?_token=98890ded-3fc2-4f19-8d09-fmin_len8f1f9f9458</a></html>')


class RegisterHandler(BaseHandler):

    @web.asynchronous
    def post(self):
        t = threading.Thread(target=self.doPost)
        t.start()

    def doPost(self):
        logging.info('-------%s start-------',__name__)
        try:
            nickname = self.get_argument('nickname',None)
            username = self.get_argument('username',None)
            password = self.get_argument('password',None)

            template_vars = {
                'nickname':nickname,
                'username':username,
                'password':password
            }
            logging.info(template_vars)
            validate_result = self.validateRegister(template_vars)

            # 验证参数是否合法
            if not validate_result:
                self.make_render('register.html',
                            code = ERROR_CODE_PARAMETER_REGISTER,
                            code_msg = CODE_MSG[ERROR_CODE_PARAMETER_REGISTER])
                return None

            # 验证姓名和用户名是否存在
            nickname_username = [nickname,username]
            check_name_result = main_db.getCountByNicknameOrUsername(nickname_username)
            if not check_name_result:
                self.make_render('register.html',
                            code = ERROR_CODE_NAME_ALREADY_EXIST_REGISTER,
                            code_msg = CODE_MSG[ERROR_CODE_NAME_ALREADY_EXIST_REGISTER])
                return None

            # 注册新用户
            password = self.get_md5(password)
            pic_addr = r"/static/image/header/" + str(random.randint(1, 5)) + r".jpg"
            user_info = [nickname,username,password,pic_addr]
            insert_result = main_db.insertUser(user_info)

            if not insert_result:
                self.make_render('register.html',
                            code = ERROR_UNKNOW_REASON_REGISTER_FAIL,
                            code_msg = CODE_MSG[ERROR_UNKNOW_REASON_REGISTER_FAIL])
                return None
            self.set_secure_cookie('user_username',username)
            self.set_secure_cookie('user_nickname',nickname)
            logging.info('user_username:%s is login in .',self.get_secure_cookie('user_username'))
            self.redirect('/')
        except :
            logging.error('user register error.',exc_info=True)

    def validateRegister(self,pkg):

        max_len = 20
        min_len = 6

        nickname = pkg.get('nickname',None)
        username = pkg.get('username',None)
        password = pkg.get('username',None)

        if not nickname or\
           not username or\
           not password:
           logging.error('register param is None.%s',pkg)
           return False

        len_nickname = len(nickname)
        len_username = len(username)
        len_password = len(password)

        if len_nickname > max_len or len_nickname == 0:
            logging.error('nickname len not legal.%s',len_nickname)
            return False
        if len_username > max_len or len_username < min_len:
            logging.error('username len not legal.%s',len_username)
            return False
        if len_password > max_len or len_password < min_len:
            logging.error('password len not legal.%s',len_password)
            return False
        return True


    def get(self):
        self.make_render('register.html')