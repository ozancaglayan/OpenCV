#!/usr/bin/python

import os
import sys
import glob
import time
import xmlrpclib


if __name__ == "__main__":
    proxy = xmlrpclib.ServerProxy("http://localhost:12345/")
    sample_directory = "samples"

    try:
        sample_directory = sys.argv[1]
    except IndexError:
        pass

    for image in glob.glob(os.path.join(sample_directory, "*")):
        image_file = open(image, "rb").read()
        print "\n%s\n%s" % (image, "-"*len(image))
        start_time = time.time()
        results = proxy.detect(xmlrpclib.Binary(image_file))
        print "Returned in %.2f seconds\n" % (time.time()-start_time)
        for line in results:
            print "\t%s" % line
