# -*- coding: utf-8 -*-

# -------------------sql-------------------

# user

SQL_INSERT_USER = "insert into s_user(user_name,user_username,user_password,user_pic_addr) values(%s,%s,%s,%s)"
SQL_GET_USER_BY_NICKNAME_OR_USERNAME = "select count(*) from s_user where   user_name=%s or user_username=%s"
SQL_GET_USER_PASSWORD_BY_USERNAME = "select * from s_user where user_username=%s"


# admin
SQL_GET_ADMIN_INFO_BY_ADMINNAME = "select * from s_admin where admin_username=%s"
SQT_GET_ALL_USER_INFO = "select * from s_user limit %s,%s"

# -------------------page code-------------------

CODE_MSG = {
    200:'成功',

    # user login | register
    2001:'注册成功,请用新账户登录',

    4001:'参数不正确',
    4002:'姓名或用户名已经存在',
    4003:'因为未知原因注册失败',
    4004:'登录失败！用户名或密码错误',


    # admin login
    4051:'登录失败！用户名或密码错误'

}

# 成功
SUCCESS_CODE = 200

SUCCESS_REGISTER = 2001

# user login | register
ERROR_CODE_PARAMETER_REGISTER = 4001
ERROR_CODE_NAME_ALREADY_EXIST_REGISTER = 4002
ERROR_UNKNOW_REASON_REGISTER_FAIL = 4003
ERROR_CODE_FOR_USERNAME_PASSWORD = 4004

# admin login
ERROR_FOR_ADMINNAME_PASSWORD = 4051


# -------------------md5 salt-------------------
SALT = "HH852"