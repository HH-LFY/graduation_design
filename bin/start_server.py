#-*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import datetime
import logging
import enviroment

from daemon import run_daemon
from time import sleep

# 启动真正的运行进程
def start_server_in_subprocess():
    import http.server as root_server
    logging.info('server start.')
    root_server.start_http_server()
    sys.exit(2)

def start_server():
    run_daemon()
    try:
        pid = os.fork()
    except OSError, e:
        logging.error('start http server is error.')
        os._exit(1)
    if pid == 0:
        start_server_in_subprocess()
        return
    while pid:
        # wait 任何一个子进程结束，都将触发该函数
        ret = os.wait()
        logging.error('Child process already stop, try to start')
        try:
            pid = os.fork()
            if pid == 0:
                start_server_in_subprocess()
                return
        except OSError, e:
            logging.error('start http server is error.')
            os._exit(1)

# 关闭所有进程
def stop_server():
    processname = sys.argv[0] + ' start'
    command = r'''ps -ef | grep "%s" | awk '{print $2}' | xargs kill -9''' % processname
    logging.info('exe command:%s', command)
    try:
        logging.info('exit the http server')
        ret = os.system(command)
    except OSError, e:
        logging.error('unknow error : %s',e)




# 入口函数，根据传入的参数做相关的操作
def entry():
    if len(sys.argv) > 1:
        op = sys.argv[1]
        if op == 'start':
            start_server()
        elif op == 'restart':
            stop_server()
            # 因为关闭进程的函数是通过 程序名称+ start 来定位需要关闭的进程的，故在启动新的进程的时候，也应该复合相关的规则
            command = "python %s start" % sys.argv[0]
            os.system(command)
        elif op == 'stop':
            stop_server()
        else:
            logging.error('unknow commont:<%s>, you should write start|stop|restart .',op)
    else:
        logging.error('unknow commont, you should write start|stop|restart .')

if __name__ == '__main__':
    entry()