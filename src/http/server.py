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
        (r'/',main.IndexHandler),
        (r'/category.html',main.CategoryHandler),
        (r'/image_detail.html',main.ImageDetailHandler),
        (r'/.*',main.ErrorHandler)
    ]

    settings = dict(
        template_path=template_path,
        static_path=static_path,
        xsrf_cookies=True,
        cookie_secret="luofengyue",
        debug=True,
        gzip=True,
    )

    application = tornado.web.Application(handlers,**settings)
    http_server = tornado.httpserver.HTTPServer(application)

    listen_port = 8888
    logging.info('listen port:%s',listen_port)
    http_server.listen(listen_port)

    logging.info('http server is start.')
    tornado.ioloop.IOLoop.instance().start()