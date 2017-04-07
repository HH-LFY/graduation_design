#-*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import datetime
import logging
import enviroment
from time import sleep

def show_process_info(mark):
    print('\n')
    logging.info('show->%s',mark)
    # logging.info('sid:%s',os.getsid())
    logging.info('gid:%s',os.getgid())
    logging.info('pid:%s',os.getpid())
    logging.info('uid:%s',os.getuid())
    print('\n')

def run_daemon():
    # logging.info('time 0 only %s is running.',os.getpid())
    try:
        pid = os.fork()

        nid = os.getpid()
        if pid:
            # logging.debug('first process is exit.')
            sys.exit(0)
    except OSError,e:
        logging.error('fork a first process is failed.')
        sys.exit(1)

    # logging.info('time 1 only %s is running.',os.getpid())
    # show_process_info(2)

    # 改变运行环境
    os.chdir('/')
    os.umask(0)
    os.setsid()

    try:
        # 第二次fork ， 因为该第一次fork出来的进程依旧可能打开终端，并且挂载在某个终端下
        pid = os.fork()
        if pid:
            # logging.debug('first child process is exit')
            sys.exit(0)
    except OSError, e:
        logging.error('fork second process is failed')
        sys.exit(1)
    logging.info('daemon is running.')


def test_main():
    while True:
        print('%s is running .' % os.getpid())
        sleep(3)
        logging.info('%s is exit.', os.getpid())
        show_process_info('1')
        sys.exit(1)

if __name__ == '__main__':
    run_daemon()
    test_main()