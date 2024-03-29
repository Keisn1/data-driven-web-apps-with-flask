from typing import Optional

from passlib.handlers.sha2_crypt import sha256_crypt as crypto

import pypi_org.data.db_session as db_session
from pypi_org.data.users import User


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()


def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    user = session.query(User).filter(User.email == email).first()
    session.commit()
    return user


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None
    user = User()
    user.name = name
    user.email = email
    user.hashed_password = hast_text(password)

    session = db_session.create_session()
    session.add(user)
    session.commit()
    return user


def hast_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text: str, plain_txt: str) -> bool:
    return crypto.verify(plain_txt, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    user = session.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_hash(user.hashed_password, password):
        return None

    return user


def find_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()
    user = session.query(User).filter(User.id == id).first()
    return user