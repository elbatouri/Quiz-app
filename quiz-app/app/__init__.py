from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from flask_bcrypt import Bcrypt



db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    from app import routes, models
    app.register_blueprint(routes.bp)
    
    # Context processor to add enumerate to Jinja2 context
    @app.context_processor
    def utility_processor():
        return dict(enumerate=enumerate)
    
    return app