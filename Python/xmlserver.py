#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

from PIL import Image

import cv2

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

from detector import CascadedDetector

PORT = 12345

detector = CascadedDetector()

def detect(image, sizeX, sizeY):
    result = []
    pil_img = Image.fromstring('RGB', size, image)
    cv_img = cv2.cv.CreateImageHeader(size, cv2.IPL_DEPTH_8U, 3)
    cv2.cv.SetData(cv_img, image, sizeX*3)
    for i,r in enumerate(detector.detect(cv_img)):
        x0,y0,x1,y1 = r
        result.append("(%d, %d) - (%d, %d)" % (x0,y0,x1,y1))

    return result
        

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", PORT))
    print "Listening on port %d" % PORT

    server.register_function(detect, "detect")
    server.serve_forever()
