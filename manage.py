import os

from  flask_script import Shell, Manager

from app import create_app

app = create_app(os.environ.get('config') or 'default')

manager = Manager(app)



if __name__ == "__main__":

    manager.run()