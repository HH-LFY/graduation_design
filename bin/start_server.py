#-*- coding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import datetime
import logging
import enviroment
import base.connection_pool_mysql as connection_pool_mysql

# connection_pool_mysql.is_running()
connection_pool_mysql.test_pooled()
