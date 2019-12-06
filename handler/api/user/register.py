# -*- coding: utf-8 -*-

import tornado
from bson import ObjectId, text_type
from tornado import gen
from tornado.web import HTTPError

from handler.api import error_status
from handler.api.base import BaseHandler
from data.collections import User, School
from util.token import token_manager

class RegisterHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self):

        # 注册用户，通过手机号验证
        mobile = self.get_argument('mobile')
        pwd = self.get_argument('password')
        nickname = self.get_argument('nickname')
        users = yield User.objects.filter(mobile=mobile).find_all()

        # 用户存在
        if len(users) != 0:
            raise HTTPError(**error_status.status_21)

        school_id = self.get_argument('school_id')
        self.validate_id(school_id)

        school = yield School.objects.get(self.get_argument('school_id'))
        self.check_none(school)

        user = User(mobile=mobile, password=pwd, nickname=nickname, school_id=ObjectId(school_id))
        yield user.save()

        user = user.to_dict()
        token = token_manager.create_token(str(user['id']))
        user['token'] = token
        self.write_json(token)


class SchoolHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @gen.coroutine
    # 学校列表
    def get(self):
        schools = yield School.objects.find_all()
        schools_dict = [school.to_dict() for school in schools]
        json_data = []
        for t in schools_dict:
            j = {
                'id': text_type(t['id']),
                'verifier': t['verifier'],
                'name': t['name'],
            }
            json_data.append(j)
        self.write_json(json_data)
