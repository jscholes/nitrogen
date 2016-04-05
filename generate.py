# Nitrogen
# Copyright (C) 2016 James Scholes
# This program is free software, licensed under the terms of the GNU General Public License (version 3 or later).
# See the file LICENSE.txt for more details.

from io import BytesIO
import logging
import os
import os.path
import sys

import requests
try:
    import ujson as json
except ImportError:
    import json


__version_info__ = (0, 1)
__version__ = '.'.join((str(val) for val in __version_info__))
logger = logging.getLogger('nitrogen.generate')
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger.addHandler(stream_handler)


def main():
    if len(sys.argv) < 2:
        print('Usage: {0} <your_api_key>'.format(__file__))
        sys.exit(1)

    logger.info('Nitrogen Generator v{0}'.format(__version__))
    api_key = sys.argv[1]
    logger.info('Using API key: {0}'.format(api_key))


if __name__ == '__main__':
    main()
