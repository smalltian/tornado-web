# -*- coding: utf-8 -*-

from handler.main import MainHandler
from handler.api.user.register import SchoolHandler
from handler.api.user.register import RegisterHandler
from handler.api.user.login import LoginHandler
from handler.api.user.login import LogoutHandler
from handler.api.user.profile import UserListHandler
from handler.api.user.profile import UserHandler
from tornado.options import options

urls = [
    [r"/", MainHandler],
    [r"/api/user/schools", SchoolHandler],
    [r"/api/user/register", RegisterHandler],
    [r"/api/user/login", LoginHandler],
    [r"/api/user/logout", LogoutHandler],
    [r"/api/user/list", UserListHandler],
    [r"/api/user", UserHandler]
    # (r"/", MainHandler)
]

for u in urls:
    u[0] = options.subpath + u[0]
