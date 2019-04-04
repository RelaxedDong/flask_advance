#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/11 19:42

from flask_script import Manager
from demo import app
from exct import db
from flask_migrate import MigrateCommand,Migrate
manager = Manager(app)
Migrate(app,db)

manager.add_command('db',MigrateCommand)
'''
    init                Creates a new migration repository
    revision            Create a new revision file.
    migrate             Alias for 'revision --autogenerate'
    edit                Edit current revision.
    merge               Merge two revisions together. Creates a new migration
                        file
    upgrade             Upgrade to a later version
    downgrade           Revert to a previous version
    show                Show the revision denoted by the given symbol.
    history             List changeset scripts in chronological order.
    heads               Show current available heads in the script directory
    branches            Show current branch points
    current             Display the current revision for each database.
    stamp               'stamp' the revision table with the given revision;
                        don't run any migrations
'''

if __name__ == '__main__':
    manager.run()