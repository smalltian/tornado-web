# -*- coding: utf-8 -*-

import time

import config
from data.redis_init import redis
from util.aes import AESCrypto


class TokenManager:

    def __init__(self, aes_key, token_timeout):
        self.crypto = AESCrypto(aes_key)
        self.timeout = token_timeout

    def create_token(self, uid):
        rt = int(time.time())
        token = self.crypto.encrypt('%d@%s' % (rt, uid))
        # token = self.crypto.encrypt(uid)
        redis.set('token:' + uid, token)
        return token

    def validate_token(self, token):
        rt = int(time.time())
        token_raw = self.crypto.decrypt(token)

        if token_raw is None:
            return False, None

        try:
            sp = token_raw.split('@')
            tk_rt = int(sp[0])
            tk_uid = sp[1]

            # 和redis苦进行对比校验，检查是否过期
            active_token = redis.get('token:' + tk_uid)
            if token != active_token:
                return False, None

            if tk_rt < rt and (rt - tk_rt) <= self.timeout:
                return True, tk_uid
            else:
                return False, None

        except Exception as e:
            print('validate token: %s' % e)
            return False, None

    @classmethod
    def clear_token(cls, uid):
        redis.delete('token:' + uid)


token_manager = TokenManager(config.AES_KEY, config.TOKEN_TIMEOUT)
