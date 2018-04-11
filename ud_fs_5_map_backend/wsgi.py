#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/flask/")

import os
activate_this = '/var/www/flask_venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import main
from main import app as application
application.secret_key = 'somescret'
