from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
import logging

logging.basicConfig()
manager = Manager(create_app)

manager.add_command('db', MigrateCommand)


def run():
    manager.run()

# if __name__ == '__main__':
#     manager.run()