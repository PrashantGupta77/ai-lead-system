from sqlalchemy.orm import Session

from src.database.db import SessionLocal
from src.database.user_model import User

from src.auth.passwords import hash_password

from src.core.config import settings


def create_default_admin():

    db: Session = SessionLocal()

    try:

        admin_username = (
            settings.ADMIN_USERNAME
            .strip()
            .lower()
        )

        existing_user = (
            db.query(User)
            .filter(
                User.username == admin_username
            )
            .first()
        )

        if existing_user:

            if existing_user.role != "ADMIN":

                existing_user.role = "ADMIN"

                existing_user.password_hash = hash_password(
                    settings.ADMIN_PASSWORD
                )

                db.commit()

                print(
                    f"Existing user promoted to ADMIN: {admin_username}"
                )

            return

        admin_user = User(
            username=admin_username,
            password_hash=hash_password(
                settings.ADMIN_PASSWORD
            ),
            role="ADMIN"
        )

        db.add(admin_user)

        db.commit()

        print(
            f"Default admin created: {admin_username}"
        )

    finally:

        db.close()