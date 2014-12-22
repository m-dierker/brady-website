#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)

pathAdd2 = '/home/brady/website'
if not pathAdd2 in sys.path:
    sys.path.insert(0, pathAdd2)
#pathAdd = '/var/www/website'
#if not pathAdd in sys.path:
#    sys.path.insert(0, '/var/www/website')

from website import app 
application = app 
