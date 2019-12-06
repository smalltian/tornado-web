# -*- coding: utf-8 -*-

import tornado
from tornado import gen
from tornado.web import HTTPError
from bson.json_util import text_type

from handler.api.base import BaseHandler
from data.collections import User


class UserListHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.coroutine
    # 用户列表
    def get(self):
        self.is_logined()

        users = yield User.objects.limit(5).find_all()
        users_dict = [user.to_dict() for user in users]
        json_data = []
        for t in users_dict:
            t['id'] = text_type(t['id'])
            t['create_time'] = text_type(t['create_time'])
            t['school_id'] = text_type(t['school_id'])
            json_data.append(t)
        self.write_json(json_data)


class UserHandler(BaseHandler):

    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.coroutine
    # 获取当前登录用户
    def get(self):
        # token认证
        uid = self.is_logined()

        user_id = self.get_argument('id', uid)
        user_id = user_id if user_id != '' else uid

        self.validate_id(user_id)

        user = yield User.objects.get(user_id)
        self.check_none(user)
        user = user.to_dict()
        user['id'] = text_type(user['id'])
        user['create_time'] = text_type(user['create_time'])
        user['school_id'] = text_type(user['school_id'])
        self.write_json(user)

    @tornado.web.asynchronous
    @gen.coroutine
    # 更新用户
    def put(self):
        uid = self.is_logined()
        user = yield User.objects.get(uid)
        self.check_none(user)

        need_edit = 0
        nickname = self.get_argument('nickname', None)
        print nickname
        if self.validate_nickname(nickname):
            user.nickname = nickname
            need_edit += 1

        gender = self.get_argument('gender', '')
        if gender in ['0', '1']:
            user.gender = int(gender)
            need_edit += 1

        description = self.get_argument('description', None)
        if self.validate_description(description):
            user.description = description
            need_edit += 1

        if need_edit != 0:
            yield user.save()

        user = user.to_dict()
        user['id'] = text_type(user['id'])
        user['create_time'] = text_type(user['create_time'])
        user['school_id'] = text_type(user['school_id'])
        self.write_json(user)

    # 对昵称限制
    @staticmethod
    def validate_nickname(nickname):
        if nickname is not None and len(nickname) > 0:
            return True
        else:
            return False

    @staticmethod
    def validate_description(description):
        if description is not None and len(description) > 0:
            return True
        else:
            return False
