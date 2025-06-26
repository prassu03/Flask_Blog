from flaskblog import create_app
from flaskblog import db
app=create_app()
# from flask import app,db
# app.app_context().push()
# db.create_all()

if __name__ == '__main__':
    with app.app_context():  # Needed for DB operations
        db.create_all()
    app.run(debug=True)