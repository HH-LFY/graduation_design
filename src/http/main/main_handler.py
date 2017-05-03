# -*- coding:utf-8 -*-

import logging
import time
import threading
import random
import os
import uuid
import datetime

from PIL import Image
from cStringIO import StringIO
from all_code import *
from tornado import *
from main_const import *
from conf import *
from base.base_handler import BaseHandler
from main.main_db import main_db
from manage.manage_db import manage_db




class IndexHandler(BaseHandler):

    @web.asynchronous
    def get(self):
        t = threading.Thread(target=self.doGet)
        t.start()

    def doGet(self):
        result = {

        }
        self.make_render('index.html')

class CategoryHandler(BaseHandler):

    @web.asynchronous
    def get(self):
        t = threading.Thread(target=self.doGet)
        t.start()

    def doGet(self):
        c_id = self.get_argument('c_id',1)
        imgs = main_db.getAllImgByCategoryId([c_id,0,CATEGORY_IMG_LIST])
        result = {
            'imgs':imgs
        }
        self.make_render('category.html',
                        result=result)

class ImageDetailHandler(BaseHandler):
    def get(self):
        self.make_render('image_detail.html')

class PersonalInfoHandler(BaseHandler):

    @web.authenticated
    def get(self):
        self.make_render('personal_info.html')

class ShareImgHandler(BaseHandler):

    @web.authenticated
    @web.asynchronous
    def post(self):
        t = threading.Thread(target=self.doPost)
        t.start()

    def doPost(self):
        u_id = self.get_secure_cookie('user_id')
        c_id = self.get_argument('c_id',1)
        imgfile = self.request.files.get('my_img')
        try:
            img = imgfile[0]
            img_name = name = str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f'))  + '_' + self.current_user + '_upload.png'
            save_path = os.path.join(USER_IMG_PATH,img_name)
            logging.info('save img: %s',save_path)
            im = Image.open(StringIO(img['body']))
            im = im.resize((1200, 800), Image.ANTIALIAS)
            im_file = StringIO()
            im.save(im_file, format='PNG')
            im_data = im_file.getvalue()
            f = open(save_path,'wb')
            f.write(im_data)

            img_addr = os.path.join(IMG_ADDR_DIRECT,img_name)
            img_addr_small = img_addr
            img_size = ''
            img_author_id = u_id
            img_category_id = c_id
            img_md5 = ''
            img_pv_count = 0
            logging.debug(img_addr)

            main_db.insertImg([img_addr,img_addr_small,img_size,img_author_id,img_category_id,img_md5,img_pv_count])

            self.make_redirect('/share_img.html',
                                code=SUCCESS_SHARE_IMG,
                                code_msg=CODE_MSG[SUCCESS_SHARE_IMG])
        except:
            logging.error('unknow error on upload img.',exc_info=True)
            self.make_redirect('/share_img.html',
                                code=ERROR_CODE_UNKNOW_REASON,
                                code_msg=CODE_MSG[ERROR_CODE_UNKNOW_REASON])

# for img in imgfile:
#       # 对文件进行重命名
#       name = str(time.strftime('%Y%m%d%'), time.localtime())\
#           + '_' + self.current_user + '_headimg.png'

#       with open('./static/uploads/' + name, 'wb') as f:
#         # image有多种打开方式，一种是 Image.open('xx.png')
#         # 另一种就是 Image.open(StringIO(buffer))
#         im = Image.open(StringIO(img['body']))
#         # 修改图片大小resize接受两个参数, 第一个是宽高的元组数据,第二个是对图片细节的处理，本文表示抗锯齿
#         im = im.resize((72, 72), Image.ANTIALIAS)
#         # 打开io 就像文件一样
#         im_file = StringIO()
#         im.save(im_file, format='png')
#         # 这是获取io中的内容
#         im_data = im_file.getvalue()
#         f.write(im_data)

    @web.authenticated
    def get(self):
        self.make_render('share_img.html')




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
            logging.debug("getUserInfoByUsername data:%s",ret)
            user_id = ret.get('user_id',None)
            self.set_secure_cookie('user_username',user_username)
            self.set_secure_cookie('user_id',str(user_id))
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
        self.clear_cookie('user_id')
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
            ret = main_db.getUserInfoByUsername([username])
            self.set_secure_cookie('user_id',str(ret.get('user_id',None)))
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