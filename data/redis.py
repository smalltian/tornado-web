# -*- coding: utf-8 -*-

import tornadoredis
import config

CONNECTION_POOL = tornadoredis.ConnectionPool(max_connections=100, wait_for_available=True)
redis = tornadoredis.Client(host=config.REDIS_HOST, port=config.REDIS_HOST, connection_pool=CONNECTION_POOL)
