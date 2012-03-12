#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import tempfile

import os


import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

import cv2
from detector import CascadedDetector

PORT = 12345

# Global face detector
detector = CascadedDetector()

def detect(image):
    result = []
    tfile_fd, tfile_path = tempfile.mkstemp(prefix='opencv-')
    open(tfile_path, "wb").write(image.data)
    os.close(tfile_fd)
    np_array = np.array(cv2.imread(tfile_path), dtype=np.uint8)
    try:
        os.unlink(tfile_path)
    except:
        print "Can't remove %s" % tfile_path

    for i,r in enumerate(detector.detect(np_array)):
        x0,y0,x1,y1 = r
        result.append("Face %d -- (%d, %d) - (%d, %d)" % (i, x0, y0, x1, y1))

    return result
        

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", PORT))
    print "Listening on port %d" % PORT

    server.register_function(detect, "detect")
    server.serve_forever()
