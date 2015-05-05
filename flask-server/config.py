import os

#Store absolute path of this file in basedir.
basedir = os.path.abspath(os.path.dirname(__file__))

#Store path of app.db by joining it with the absolute path calculated above.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#Store path for directory in which migration data files are stored.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
