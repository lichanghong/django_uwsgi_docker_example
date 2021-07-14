#!/bin/bash
uwsgi --ini  /var/www/html/packing/uwsgi.ini
 
tail -f /dev/null