from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_wtf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_heroku import Heroku
from flask_ckeditor import CKEditor
from flask_migrate import Migrate


heroku = Heroku()
debug_toolbar = DebugToolbarExtension()
mail = Mail()
csrf = CsrfProtect()
db = SQLAlchemy()
login_manager = LoginManager()
ckeditor = CKEditor()
migrate = Migrate()