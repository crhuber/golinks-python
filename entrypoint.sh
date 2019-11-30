#!/bin/sh
flask db upgrade
exec gunicorn manage:app -w 4 -b 0.0.0.0:5000 --access-logfile -