# -*- coding: utf-8 -*-
import tornado
from tornado import gen
from tornado.web import HTTPError
from bson.json_util import text_type

from util.token import token_manager
from handler.api import error_status
from handler.api.base import BaseHandler
from data.collections import User
from data.redis import redis

class LoginHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        mobile = self.get_argument('mobile', None)
        pwd = self.get_argument('password', None)
        user = None
        if mobile is None or mobile == '' or pwd is None or pwd == '':
            # 是否过期，或有没有登录
            uid = self.is_logined()
            user = yield User.objects.get(uid)
        else:
            # 登录
            users = yield User.objects.filter(mobile=mobile).find_all()
            if len(users) == 0:
                # 未找到用户
                raise HTTPError(**error_status.status_22)

            if users[0].password != pwd:
                raise HTTPError(**error_status.status_23)

            user = users[0]

        print user

        # 登录成功
        user = user.to_dict()
        token = token_manager.create_token(str(user['id']))
        user['token'] = token
        user['id'] = text_type(user['id'])
        user['create_time'] = text_type(user['create_time'])
        user['school_id'] = text_type(user['school_id'])
        self.write_json(user)


class LogoutHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.coroutine
    def delete(self):

        uid = self.is_logined()

        token_manager.clear_token(uid)
        self.write_json({})
