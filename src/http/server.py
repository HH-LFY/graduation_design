# -*- coding:utf-8 -*-

import os
import sys
import logging
import time

import tornado.web
import tornado.httpserver
import tornado.ioloop

# handler module
import http.main.main_handler as main
import http.manage.manage_handler as manage

def start_http_server():
    logging.info('Try to start tornado.')

    # 获取相关路径
    file_path   = os.path.realpath(__file__)
    http_path   = os.path.dirname(file_path)
    src_path    = os.path.dirname(http_path)
    root_path   = os.path.split(src_path)[0]
    template_path = os.path.join(root_path,'template')
    static_path = os.path.join(root_path,'template/static')

    # tornado http 配置
    handlers = [
        # user
        (r'/',main.IndexHandler),
        (r'/category.html',main.CategoryHandler),
        (r'/image_detail.html',main.ImageDetailHandler),
        (r'/personal_info.html',main.PersonalInfoHandler),
        (r'/login.html',main.LoginHandler),
        (r'/login_out',main.LoginOutHandler),
        (r'/register.html',main.RegisterHandler),
        (r'/share_img.html',main.ShareImgHandler),
        (r'/op_img',main.OpImgHandler),
        (r'/add_disscuss',main.AddDisscussHandler),

        # admin
        (r'/manage_login.html',manage.ManageLoginHandler),
        (r'/manage/login_out',manage.ManageLoginOutHandler),
        (r'/manage/user_manage.html',manage.ManageUserHandler),
        (r'/manage/img_manage.html',manage.ManageImgHandler),
        (r'/manage/img_op',manage.ManageImgOpHandler),
        (r'/manage/category_manage.html',manage.ManageCategoryHandler),
        (r'/manage/category_manage/add',manage.AddCategoryHandler),
        (r'/manage/discuss_manage.html',manage.ManageDiscussHandler),
        # (r'/manage/discuss_manage/op',manage.ManageDiscussHandler),
        # (r'/.*',main.TestHandler),
        (r'/.*',main.ErrorHandler)
    ]

    settings = dict(
        template_path=template_path,
        static_path=static_path,
        xsrf_cookies=True,
        cookie_secret="luofengyue",
        debug=True,
        gzip=True,
        login_url="/login.html",
    )

    application = tornado.web.Application(handlers,**settings)
    http_server = tornado.httpserver.HTTPServer(application)

    listen_port = 8888
    logging.info('listen port:%s',listen_port)
    http_server.listen(listen_port)

    logging.info('http server is start.')
    tornado.ioloop.IOLoop.instance().start()
