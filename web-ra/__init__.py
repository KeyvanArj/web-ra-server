from flask import Flask

from .views import auth

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Register Authentication View 
    app.register_blueprint(auth.auth_blueprint)
    
    @app.route('/')
    def version():
        return '1.0.0'
    
    return app

