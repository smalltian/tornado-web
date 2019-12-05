# -*- coding: utf-8 -*-

from motorengine import connect, Document, StringField, IntField
from tornado import gen, ioloop
import config

from data.collections import School

@gen.coroutine
def create_schools():
    schools = [
        {'name': u'北京大学', 'verifier': u''},
        {'name': u'清华大学', 'verifier': u''},
        {'name': u'天津大学', 'verifier': u''},
        {'name': u'南开大学', 'verifier': u''}
    ]

    for school in schools:
        print(school)
        yield School(**school).save()


@gen.coroutine
def init_db():
    yield create_schools()

    io_loop.stop()


if __name__ == "__main__":
    io_loop = ioloop.IOLoop.instance()
    connect(config.DB_NAME, host=config.DB_HOST, port=config.DB_PORT, io_loop=io_loop)
    print("connect mongodb success")
    io_loop.add_timeout(1, init_db)
    io_loop.start()
