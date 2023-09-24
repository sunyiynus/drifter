#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import datetime


pDir = 'D:\\1.0_CODE_PROJECT\\auto_dir\\'
localtime = time.localtime(time.time())
# 格式化成2016-03-20 11:45:39形式
beginTime = time.strftime("%Y%m%d", time.localtime())
endTime = (datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y%m%d")

directory =pDir + beginTime +  "-" + endTime
os.mkdir(directory)
