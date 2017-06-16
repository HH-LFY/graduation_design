
[TOC]

# 介绍
> 这是一个壁纸共享网站

# 网站所需要的基础运行环境
    操作系统：Ubuntu 16.04
    数据库：MySQL 5.5
    Python解释器版本：Python 2.7
    Python外部依赖包：MySQLdb

# 网站具体搭建方法
    1.  打开 doc/database_design.sql ,该文件中的数据是mysql数据库表的创建代码，将其中的代码复制到mysql客户端执行，便能够创建出本网站所需要的数据库和表。
    2.  修改conf目录下的conf.py 文件，该文件下有一个CONF的变量，将其中 db_mysql 中的的用户名和密码改为当前运行环境下的mysql的用户名和密码即可。
    3.  cd 到bin目录下，执行python start_server.py start 命令。此时打开log目录下的server.log文件，如果文件最后一行写着http server is start。那么网站算是成功启动了。
    4.  在浏览器中访问http://127.0.0.1:8888/ 即可
