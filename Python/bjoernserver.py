#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

# Bjoern is a Fast and Ultra-Lightweight Asynchronous HTTP/1.1 WSGI Server
# https://github.com/jonashaag/bjoern
import bjoern

TEMPLATE = """\
<body>
<html>
<h1>Face Detection Server</h1>
<img src='file:///home/ozan/git/OpenCV/Python/05.jpg'/>
</html>
</body>
"""

def detection(env, sr):
    sr('200 ok', [])
    return TEMPLATE

def wsgi_app(env, start_response):
    return detection(env, start_response)


if __name__ == "__main__":
    bjoern.run(wsgi_app, '0.0.0.0', 12345)
