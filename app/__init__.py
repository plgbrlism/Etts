from flask import Flask
from .db import close_db, get_db

def create_app():
    app = Flask(__name__)

    # 1. Register Database Teardown
    app.teardown_appcontext(close_db)

    # 2. Register Modules (Blueprints)
    from app.modules.library.routes import library_bp
    app.register_blueprint(library_bp)

    # 3. Initialize DB (Quick check to create tables)
    with app.app_context():
        init_db()

    return app

def init_db():
    """Runs schema.sql if tables don't exist"""
    db = get_db()
    cursor = db.cursor()
    try:
        with open('app/schema.sql', 'r') as f:
            cursor.execute(f.read())
        db.commit()
    except Exception as e:
        print(f"DB Init Warning: {e}")