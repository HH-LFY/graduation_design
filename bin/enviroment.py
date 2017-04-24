#-*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import datetime
import logging
import subprocess

# 设置运行环境

file_path   = os.path.realpath(__file__)
bin_path    = os.path.dirname(file_path)
root_path   = os.path.split(bin_path)[0]
src_path    = os.path.join(root_path,'src')
conf_path   = os.path.join(root_path,'conf')
log_path    = os.path.join(root_path,'log')

python_path = os.getenv('PYTHONPATH')

if python_path == None:
    python_path = bin_path
else:
    python_path += ':' +bin_path

python_path += ':' + src_path
python_path += ':' + conf_path
python_path += ':' + log_path

os.putenv('PYTHONPATH',python_path)

if os.getenv('PYTHONPATH') == None:
    os.environ['PYTHONPATH'] = python_path
    try:
        from base import connection_pool_mysql
    except ImportError, e:
        # print('use os.environ , import base is error , python path will add in PATY~')
        sys.path.append(src_path)
        sys.path.append(log_path)
        sys.path.append(conf_path)
        sys.path.append(bin_path)
        from base import connection_pool_mysql

    else:
        print('add in path error \ndon\'t running..\n system will exit.')
        sys.exit(0)
    finally:
        pass


# 设置 logging
log_file = os.path.join(log_path,'server.log')
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(levelname)s::%(asctime)s %(filename)s[line:%(lineno)d] fun(%(funcName)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# 重定向 stderr 和 stdout 到同一个 log 文件
old_out = os.dup(sys.stdout.fileno())
old_err = os.dup(sys.stderr.fileno())
with open(log_file, "a") as fp:
    fd = fp.fileno()
    os.dup2(fd, sys.stdout.fileno())
    os.dup2(fd, sys.stderr.fileno())

logging.info("<logging module> is ok!")


if __name__ == '__main__':
    print(__file__)
    print(bin_path)
    print(root_path)
    print(src_path)
    print(conf_path)
    print(log_path)
    print(python_path)
    print(os.getenv('PYTHONPATH'))
    logging.warning('this is warning!')