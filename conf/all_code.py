# -*- coding: utf-8 -*-

# -------------------sql-------------------

# user

INSERT_USER = "insert into s_user(user_name,user_username,user_password,user_pic_addr) values(%s,%s,%s,%s)"
GET_USER_BY_NICKNAME_OR_USERNAME = "select count(*) from s_user where   user_name=%s or user_username=%s"

# -------------------page code-------------------

CODE_MSG = {
    200:'成功',

    2001:'注册成功,请用新账户登录',

    4001:'参数不正确',
    4002:'姓名或用户名已经存在',
    4003:'因为未知原因注册失败'
}

# 成功
SUCCESS_CODE = 200

# 注册成功
SUCCESS_REGISTER = 2001

# 注册时 输入的参数不正确
ERROR_CODE_PARAMETER_REGISTER = 4001

# 注册时候姓名或者用户名已经存在
ERROR_CODE_NAME_ALREADY_EXIST_REGISTER = 4002

# 因为未知原因注册失败
ERROR_UNKNOW_REASON_REGISTER_FAIL = 4003

# -------------------md5 salt-------------------
SALT = "HH852"