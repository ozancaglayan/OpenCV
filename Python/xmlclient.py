#!/usr/bin/python

import sys
import xmlrpclib

from PIL import Image

proxy = xmlrpclib.ServerProxy("http://localhost:12345/")

image = Image.open(sys.argv[1])
proxy.detect(image.tostring(), image.size[0], image.size[1])
