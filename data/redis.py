# -*- coding: utf-8 -*-

import redis
import config

redis = redis.Redis(
    connection_pool=redis.Connection(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=0
    )
)
