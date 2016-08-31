# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import os

# Database Config
db_engine = 'django.db.backends.postgresql_psycopg2'
db_name = 'generic'
db_user = 'postgres'
db_password = 'test1234'
db_host = '127.0.0.1'
db_port = '5432'
db_test = 'generictest'

# General Config
DEBUG = True
base_dir = os.path.dirname(os.path.abspath(__file__))


def create_gitignore():
    gitignore_content = """
    ### Django ###
    *.log
    *.pot
    *.pyc
    __pycache__/
    local_settings.py
    db.sqlite3
    media
    ### Ignore all local_settings ###
    *_settings.py
    """
    print("Creating .gitignore ...")
    with open(".gitignore", "w+") as gitignore:
        gitignore.write(gitignore_content)


def get_secret_key():
    if os.path.exists(base_dir.split("/")[-1] + "/settings.py"):
        SECRET_KEY = ""
        with open(base_dir.split("/")[-1] + "/settings.py", "w+") as settings:
            print("Searching for SECRET_KEY in settings.py ...")
            for line in settings:
                if "SECRET_KEY" in line:
                    SECRET_KEY = line
                    print("Yay!!! Found SECRET KEY!")
                    return SECRET_KEY
    return ''


def create_local_settings(file_name='local_settings_sample.py', db_engine='',
                          db_name='', db_user='', db_password='', db_host='',
                          db_test='', db_port='', DEBUG=True, SECRET_KEY=''):
    with open(base_dir.split("/")[-1] + "/" + file_name, "w+") as \
                                        local_settings:
        print("Generating " + file_name + " ...")
        local_settings_content = """
        DEBUG = """ + str(DEBUG) + """
        DATABASES = {
            'default': {
                'ENGINE': '""" + db_engine + """',
                'NAME': '""" + db_name + """',
                'USER': '""" + db_user + """',
                'PASSWORD': '""" + db_password + """',
                'HOST': '""" + db_host + """',
                'PORT': '""" + db_port + """',
                'TEST': {
                    'NAME': '""" + db_test + """',
                },
            }
        }
        """
        local_settings_content = 'SECRET_KEY = ' + SECRET_KEY + "\n" + \
            local_settings_content
        local_settings.write(local_settings_content)


create_gitignore()
# local_settings_sample.py
create_local_settings()
# local_settings.py
create_local_settings('local_settings.py', db_engine, db_name, db_user,
                      db_password, db_host, db_test, db_port, DEBUG,
                      get_secret_key())
