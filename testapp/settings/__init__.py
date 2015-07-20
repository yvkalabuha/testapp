

# -*- coding: utf-8 -*-

# import logging
# from .logging import *

print(__file__, 'loaded')

try:
    from .local import *
except ImportError as e:
    print '**** local.py not found ***'
    # logging.error("Can't find local.py settings")
    print e
