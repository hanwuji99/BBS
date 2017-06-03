#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.app

"""
建立一个软连接
ln -s /var/www/BBS/BBS.supervisor.conf /etc/supervisor/conf.d/BBS.supervisor.conf

ln -s /var/www/BBS/BBS.nginx /etc/nginx/sites-enabled/BBS

ln -s /var/www/BBS/redis-server.conf /etc/supervisor/conf.d/redis-server.conf

ln -s /var/www/BBS/mongod.conf /etc/supervisor/conf.d/mongod.conf



➜  ~ cat /etc/supervisor/conf.d/BBS.supervisor.conf

[program:BBS]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/BBS
autostart=true
autorestart=true


gunicorn.config.py

bind = '0.0.0.0:2001'
pid = '/tmp/BBS.pid'
"""
