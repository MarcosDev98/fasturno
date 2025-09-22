from flask import Flask
import os
from configs.database import db
from routes.usuario import usuarios_bp


def create_app():
  app = Flask(__name__)
  base_dir = os.path.abspath(os.path.dirname(__file__))
  app.register_blueprint(usuarios_bp)
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "fasturno.db")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.init_app(app)

  with app.app_context():
    from models.Usuario import Usuario
    db.create_all()

  return app
  
if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)