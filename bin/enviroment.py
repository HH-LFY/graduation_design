#-*- conding:utf-8 -*-
#!/usr/bin/env python

import os
import sys
import datetime
import logging

file_path = os.path.realpath(__file__)
bin_path = os.path.dirname(file_path)


if __name__ == '__main__':
    print(__file__)
    print(bin_path)