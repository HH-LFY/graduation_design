# -*- coding: utf-8 -*-

# -------------------sql-------------------

# user

SQL_INSERT_USER = "insert into s_user(user_name,user_username,user_password,user_pic_addr) values(%s,%s,%s,%s)"
SQL_GET_USER_BY_NICKNAME_OR_USERNAME = "select count(*) from s_user where   user_name=%s or user_username=%s"
SQL_GET_USER_PASSWORD_BY_USERNAME = "select * from s_user where user_username=%s"
SQL_GET_ALL_IMG_INFO_BY_CATEGORY_ID = '''
select *
from s_img as a
where a.img_category_id=%s and
a.img_id > %s
limit %s
'''

SQL_GET_IMG_BY_DATE = '''
select *
from s_img
order by img_id desc
'''

SQL_GET_IMG_PRAISE_NUM = '''
select count(user_id)
from s_img_praise
where img_id in (%s)
group by img_id
'''

# user-img
SQL_INSERT_IMG = "insert into s_img(img_addr,img_addr_small,img_size,img_author_id,img_category_id,img_md5,img_pv_count) values(%s,%s,%s,%s,%s,%s,%s)"
SQL_GET_IMG_BY_IMGID = '''
select * from s_img where img_id = %s
'''
SQL_INSERT_PRAISE_IMG = '''
insert into s_img_praise(user_id,img_id) values(%s,%s)
'''

SQL_INSERT_COLLET_IMG = '''
insert into s_img_collet(user_id,img_id) values(%s,%s)
'''


# admin
SQL_GET_ADMIN_INFO_BY_ADMINNAME = "select * from s_admin where admin_username=%s"
SQT_GET_ALL_USER_INFO = "select * from s_user limit %s,%s"
SQL_INSERT_CATEGORY = "insert into s_category(category_pid,category_name,reserve_1) values(%s,%s,%s)"
SQL_GET_ALL_CATEGORY_INFO = "select * from s_category limit %s,%s"

# -------------------page code-------------------

CODE_MSG = {
    200:'成功',

    # user login | register
    2001:'注册成功,请用新账户登录',
    2002:'上传壁纸成功',

    4001:'参数不正确',
    4002:'姓名或用户名已经存在',
    4003:'因为未知原因注册失败',
    4004:'登录失败！用户名或密码错误',
    4005:'因为未知原因操作失败',


    # admin login
    4051:'登录失败！用户名或密码错误',
    4052:'未知的原因导致添加类别失败',
    4053:'输入的分类名称不能为空'

}

# 成功
SUCCESS_CODE = 200

SUCCESS_REGISTER = 2001
SUCCESS_SHARE_IMG = 2002

# user login | register
ERROR_CODE_PARAMETER_REGISTER = 4001
ERROR_CODE_NAME_ALREADY_EXIST_REGISTER = 4002
ERROR_UNKNOW_REASON_REGISTER_FAIL = 4003
ERROR_CODE_FOR_USERNAME_PASSWORD = 4004
ERROR_CODE_UNKNOW_REASON = 4005

# admin login
ERROR_FOR_ADMINNAME_PASSWORD = 4051
ERROR_UNKNOW_REASON_ADD_CATEGORY_FAIL = 4052
ERROR_CATEGORY_NAME_NOT_NULL = 4053


# -------------------md5 salt-------------------
SALT = "HH852"