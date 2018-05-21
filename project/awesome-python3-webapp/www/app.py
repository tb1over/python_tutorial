#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import json
import logging
import os
import time
from datetime import datetime

from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    # 定义一个webAPP:
    app = web.Application(loop=loop)
    # 添加get方法，就是常规上网方式:
    app.router.add_route('GET', '/', index)
    # 用异步协程方法创建一个网络服务
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # 设置网络登陆信息
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()