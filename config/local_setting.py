# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/food_db?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SERVER_PORT=5000

RELEASE_VERSION="20180729001"

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

IGNORE_URLS = [
    "^/user/login",
]

API_IGNORE_URLS = [
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

AUTH_COOKIE_NAME = "mooc_food"


PAGE_SIZE = 50
PAGE_DISPLAY = 10


STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wx7a6552e4f5ca0514',
    'appkey':'7379cfd345ca748731f207b8ccccb061',
    'paykey':'xxxxxxxxxxxxxx换自己的',
    'mch_id':'xxxxxxxxxxxx换自己的',
    'callback_url':'/api/order/callback'
}




APP = {
    'domain':'http://127.0.0.1:5000'
}

PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}