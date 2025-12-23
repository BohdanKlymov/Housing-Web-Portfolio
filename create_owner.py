from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    owner = User(
        name="Bohdan Klymov",
        email="bohdanklymov339@gmail.com",
        password=generate_password_hash("CHANGE_THIS_PASSWORD"),
        is_owner=True
    )
    db.session.add(owner)
    db.session.commit()

    print("Owner account created successfully.")
