#-*- coding: utf-8 -*-
#!/usr/bin/env python



#配置项
CONF={
    'db_mysql':{
        'host'  : 'localhost',
        'user'  : 'root',
        'passwd': '123456',
        'db'    : 'sys',
        'port'  : 3306,
    }
}

if __name__ == '__main__':
    print(CONF.__str__())