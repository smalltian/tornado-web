# -*- coding: utf-8 -*-

import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# mongodb config
DB_HOST = 'localhost'
DB_PORT = 27017
DB_NAME = 'tornado_web'
DB_USER = 'tornado'
DB_PWD = 'tornado12345'

# redis config
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# qinniuyun config
QINIU_AK = ''
QINIU_SK = ''
QINIU_BUCKET_NAME = ''
QINIU_HOST = ''
QINIU_STATIC_URL = QINIU_HOST + ''

# 访问令牌
AES_KEY = 'your 32 byte aes key'
TOKEN_TIMEOUT = 60 * 60 * 24 * 30


