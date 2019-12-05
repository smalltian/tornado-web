# -*- coding: utf-8 -*-

from handler.main import MainHandler
from tornado.options import options

urls = [
    [r"/", MainHandler]
    # (r"/", MainHandler)
]

for u in urls:
    u[0] = options.subpath + u[0]
